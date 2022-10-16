import pytest

from app.seeds import SizeTemplate
from app.controllers.size import SizeController


def test_seeder_create_sizes_in_db(app):
    seeder = SizeTemplate()
    data = seeder.test_seeder()
    data_from_seeder = []
    for item in data:
        item = {'name': item.name, 'price': item.price}
        created_beverage, _ = SizeController.create(item)
        data_from_seeder.append(created_beverage)
    pytest.assume(len(data) != 0)
    possible_items = [
        'Tomato', 'Bacon', 'Pepperoni', 'Corn', 'Meat', 'Mushrooms',
        'Pinnapple', 'Onion', 'Cheese', 'Spinach', 'Anchovies', 'Garlic'
        ]
    data_in_db, error = SizeController.get_all()
    pytest.assume(error is None)
    pytest.assume(len(data_in_db) != 0)
    for ingredient in data_in_db:
        pytest.assume(ingredient['name'] in possible_sizes)
