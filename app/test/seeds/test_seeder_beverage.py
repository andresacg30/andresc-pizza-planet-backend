import pytest

from app.seeds import BeverageTemplate
from app.controllers.beverage import BeverageController


def test_seeder_create_beverages_in_db(app):
    seeder = BeverageTemplate()
    data = seeder.test_seeder()
    data_from_seeder = []
    for item in data:
        item = {'name': item.name, 'price': item.price}
        created_beverage, _ = BeverageController.create(item)
        data_from_seeder.append(created_beverage)
    pytest.assume(len(data) != 0)
    possible_beverages = ['Sprite', 'Natural Juice', 'CocaCola', 'Water', 'Beer', 'Ice Tea']
    data_in_db, error = BeverageController.get_all()
    pytest.assume(error is None)
    pytest.assume(len(data_in_db) != 0)
    for ingredient in data_in_db:
        pytest.assume(ingredient['name'] in possible_beverages)
