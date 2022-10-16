import pytest

from app.controllers.order import OrderController


def test_seeder_create_ingredients_in_db(app):
    seeder = OrderTemplate()
    data = seeder.test_seeder()
    data_from_seeder = []
    for item in data:
        item = {'name': item.name, 'price': item.price}
        created_ingredient, _ = OrderController.create(item)
        data_from_seeder.append(created_ingredient)
