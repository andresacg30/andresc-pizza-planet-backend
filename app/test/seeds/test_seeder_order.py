import pytest

from app.seeds import OrderTemplate


def test_order_seeder_creates_orders_in_db(app):
    seeder = OrderTemplate()
    order_model = {
        "_id": None,
        "client_name": None,
        "client_dni": None,
        "client_address": None,
        "client_phone": None,
        "date": None,
        "total_price": None,
        "size_id": None,
    }
    order_detail_model = {
        "_id": None,
        "ingredient_price": None,
        "order_id": None,
        "ingredient_id": None,
        "beverage_id": None,
    }
    order, order_details = seeder.generate_info()
    pytest.assume(len(order) != 0)
    pytest.assume(len(order_details) != 0)
    for item in order:
        for key in order_model.keys():
            pytest.assume(key in item.__dict__.keys())
    for item in order_details:
        for key in order_detail_model.keys():
            pytest.assume(key in item.__dict__.keys())
