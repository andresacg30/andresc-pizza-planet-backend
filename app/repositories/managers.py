from typing import Any, List, Optional, Sequence

from sqlalchemy.sql import text, column
from sqlalchemy import func, desc

from .models import Beverage, Ingredient, Order, OrderDetail, Size, db
from .serializers import BeverageSerializer, IngredientSerializer, OrderSerializer, SizeSerializer, ma


class BaseManager:
    model: Optional[db.Model] = None
    serializer: Optional[ma.SQLAlchemyAutoSchema] = None
    session = db.session

    @classmethod
    def get_all(cls):
        serializer = cls.serializer(many=True)
        _objects = cls.model.query.all()
        result = serializer.dump(_objects)
        return result

    @classmethod
    def get_by_id(cls, _id: Any):
        entry = cls.model.query.get(_id)
        return cls.serializer().dump(entry)

    @classmethod
    def create(cls, entry: dict):
        serializer = cls.serializer()
        new_entry = serializer.load(entry)
        cls.session.add(new_entry)
        cls.session.commit()
        return serializer.dump(new_entry)

    @classmethod
    def update(cls, _id: Any, new_values: dict):
        cls.session.query(cls.model).filter_by(_id=_id).update(new_values)
        cls.session.commit()
        return cls.get_by_id(_id)


class SizeManager(BaseManager):
    model = Size
    serializer = SizeSerializer


class IngredientManager(BaseManager):
    model = Ingredient
    serializer = IngredientSerializer

    @classmethod
    def get_by_id_list(cls, ids: Sequence):
        return (
            cls.session.query(cls.model).filter(cls.model._id.in_(set(ids))).all() or []
        )


class OrderManager(BaseManager):
    model = Order
    serializer = OrderSerializer

    @classmethod
    def create(cls, order_data: dict, ingredients: List[Ingredient], beverages: List[Beverage]):
        new_order = cls.model(**order_data)
        cls.session.add(new_order)
        cls.session.flush()
        cls.session.refresh(new_order)
        cls.session.add_all(
            (
                OrderDetail(
                    order_id=new_order._id,
                    ingredient_id=ingredient._id,
                    ingredient_price=ingredient.price,
                    beverage_id=beverage._id,
                    beverage_price=beverage.price,
                )
                for beverage in beverages for ingredient in ingredients
            )
        )
        cls.session.commit()
        return cls.serializer().dump(new_order)

    @classmethod
    def update(cls):
        raise NotImplementedError(f"Method not suported for {cls.__name__}")


class IndexManager(BaseManager):
    @classmethod
    def test_connection(cls):
        cls.session.query(column("1")).from_statement(text("SELECT 1")).all()


class BeverageManager(BaseManager):
    model = Beverage
    serializer = BeverageSerializer

    @classmethod
    def get_by_id_list(cls, ids: Sequence):
        return (
            cls.session.query(cls.model).filter(cls.model._id.in_(set(ids))).all() or []
        )


class ReportManager(BaseManager):

    @classmethod
    def get_top_clients(cls):
        limit = 3
        query = cls.session.query(
            Order.client_name,
            func.sum(Order.total_price).label('total')
        ).group_by(Order.client_name).order_by(desc('total')).limit(limit).all()
        return list(map(lambda x: {'client_name': x[0], 'amount_spent': x[1]}, query))

    @classmethod
    def get_month_with_most_revenue(cls):
        query = cls.session.query(
            func.strftime('%Y-%m', Order.date).label('month'),
            func.sum(Order.total_price).label('amount')
        ).group_by('month').order_by(desc('amount')).first()

        if not query:
            return

        month, amount = query
        return {
            'month': month,
            'amount': amount
        }

    @classmethod
    def get_most_requested_ingredient(cls):
        query = cls.session.query(
            OrderDetail.ingredient_id, func.count(OrderDetail.ingredient_id).label('qty')
        ).group_by(OrderDetail.ingredient_id).order_by(desc('qty')).first()

        if not query:
            return

        most_requested_ingredient_id, quantity = query
        most_requested_ingredient_id = IngredientManager.get_by_id(most_requested_ingredient_id)
        return {
            'ingredient': most_requested_ingredient_id,
            'quantity': quantity
        }
