import pytest

from app.seeds import IngredientSeeder
from app.controllers.ingredient import IngredientController


def test_seeder_create_ingredients_in_db(app):
    seeder = IngredientSeeder()
    seeder.generate_info()
    seeder.get_data()
    data = seeder.data_to_add
    data_from_seeder = []
    for item in data:
        item = {'name': item.name, 'price': item.price}
        created_ingredient, _ = IngredientController.create(item)
        data_from_seeder.append(created_ingredient)
    possible_ingredients = ['Tomato', 'Bacon', 'Pepperoni', 'Corn', 'Meat', 'Mushrooms']
    data_in_db, error = IngredientController.get_all()
    pytest.assume(error is None)
    pytest.assume(len(data_in_db) != 0)
    for ingredient in data_in_db:
        pytest.assume(ingredient['name'] in possible_ingredients)


def test_seeder_create_beverages_in_db(app):
    seeder = BeverageSeeder()
    seeder.generate_info()
    seeder.get_data()
    data = seeder.data_to_add

