import pytest

from app.seeds import IngredientTemplate
from app.controllers.ingredient import IngredientController


def test_ingredient_seeder_creates_ingredients_in_db(app):
    seeder = IngredientTemplate()
    data = seeder.data_to_list()
    data_from_seeder = []
    for item in data:
        item = {'name': item.name, 'price': item.price}
        created_ingredient, _ = IngredientController.create(item)
        data_from_seeder.append(created_ingredient)
    pytest.assume(len(data) != 0)
    possible_ingredients = [
        'Tomato', 'Bacon', 'Pepperoni', 'Corn', 'Meat', 'Mushrooms',
        'Pinnapple', 'Onion', 'Cheese', 'Spinach', 'Anchovies', 'Garlic'
        ]
    data_in_db, error = IngredientController.get_all()
    pytest.assume(error is None)
    pytest.assume(len(data_in_db) != 0)
    for ingredient in data_in_db:
        pytest.assume(ingredient['name'] in possible_ingredients)
