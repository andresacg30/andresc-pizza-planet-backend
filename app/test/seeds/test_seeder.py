import pytest
from app.controllers.ingredient import IngredientController
from app.seeds.seeder import IngredientSeeder, seed_database


def test_seeder_create_ingredients_in_db(app):
    entry, error = seed_database(IngredientSeeder(), IngredientController)
    pytest.assume(error is None)
