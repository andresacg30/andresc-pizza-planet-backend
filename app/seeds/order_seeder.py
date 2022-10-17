from typing import List
from flask_seeder import Seeder, Faker, generator
from datetime import datetime, timezone

from app.repositories.models import Order, OrderDetail
from app.seeds.utils.generator_extension import DateSequence, NameSequence
from app.seeds.base_seeder import BaseSeeder
from app.seeds import SizeTemplate, IngredientTemplate, BeverageTemplate


class OrderTemplate(BaseSeeder):

    number_of_items: int = 200
    orders_created = []
    order_details_created = []
    orders: List
    order_details: List

    def generate_info(self):
        faker_order = Faker(
            cls=Order,
            init={
                "_id": generator.Sequence(end=self.number_of_items),
                "client_name": NameSequence(),
                "client_dni": generator.String('\c{8}-\c{8}'),  # noqa W605
                "client_address": generator.String('[5-9]{4}-[0-9]{9}'),
                "client_phone": generator.String('[5-9]{4}-[0-9]{9}'),
                "date": DateSequence(start_date=datetime(2021, 12, 1, tzinfo=timezone.utc)),
                "total_price": 0,
                "size_id": generator.Integer(start=1, end=6)
            }
        )

        faker_order_details = Faker(
            cls=OrderDetail,
            init={
                "_id": generator.Sequence(end=self.number_of_items),
                "ingredient_price": 0,
                "order_id": generator.Integer(start=1, end=self.number_of_items),
                "ingredient_id": generator.Integer(start=1, end=12),
                "beverage_id": generator.Integer(start=1, end=11)
            }
        )

        self.orders = [
            order for order in faker_order.create(self.number_of_items)
            ]
        self.order_details = [
            order_detail for order_detail in faker_order_details.create(self.number_of_items)
            ]

        def build_order():
            sizes = SizeTemplate().data_to_list()
            ingredients = IngredientTemplate().data_to_list()
            beverages = BeverageTemplate().data_to_list()
            orders_to_insert = []
            order_details_to_insert = []

            for order_detail in self.order_details:
                order_detail.ingredient_price = sum(
                    [ingredient.price for ingredient in ingredients
                        if ingredient._id == order_detail.ingredient_id])

            for order_detail in self.order_details:
                order_detail.beverage_price = sum(
                    [beverage.price for beverage in beverages
                        if beverage._id == order_detail.beverage_id])
                order_details_to_insert.append(order_detail)

            for order in self.orders:
                ingredients_price = sum([
                    detail.ingredient_price for detail in self.order_details
                    if detail.order_id == order._id]
                    )

                size_price = sum(
                    [size.price for size in sizes if size._id == order.size_id]
                    )

                beverages_price = sum([
                    detail.beverage_id for detail in self.order_details
                    if detail.order_id == order._id]
                    )

                order.total_price = ingredients_price + size_price + beverages_price
                orders_to_insert.append(order)

            return orders_to_insert, order_details_to_insert
        orders_to_insert, order_details_to_insert = build_order()
        return orders_to_insert, order_details_to_insert

    def insert_data(self):
        orders_to_insert, order_details_to_insert = self.generate_info()
        for item in orders_to_insert:
            self.db.session.add(item)
        for item in order_details_to_insert:
            self.db.session.add(item)


class ZOrderSeeder(OrderTemplate, Seeder):

    def run(self):
        self.insert_data()
