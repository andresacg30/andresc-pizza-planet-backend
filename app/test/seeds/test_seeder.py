import pytest

from app.seeds import IngredientSeeder, BeverageSeeder
from app.controllers.ingredient import IngredientController
from app.controllers.beverage import BeverageController


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
