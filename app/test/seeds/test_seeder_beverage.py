import pytest

from app.seeds import BeverageTemplate
from app.controllers.beverage import BeverageController


def test_beverage_seeder_creates_beverages_in_db(app):
    seeder = BeverageTemplate()
    data = seeder.data_to_list()
    data_from_seeder = []
    for item in data:
        item = {'name': item.name, 'price': item.price}
        created_beverage, _ = BeverageController.create(item)
        data_from_seeder.append(created_beverage)
    pytest.assume(len(data) != 0)
    possible_beverages = [
        'Sprite', 'Orange Juice', 'CocaCola', 'Water', 'Beer', 'Ice Tea',
        'Apple Juice', 'Fanta', 'Dr. Pepper', 'Chocolate Milk', 'Wine'
        ]
    data_in_db, error = BeverageController.get_all()
    pytest.assume(error is None)
    pytest.assume(len(data_in_db) != 0)
    for beverage in data_in_db:
        pytest.assume(beverage['name'] in possible_beverages)
