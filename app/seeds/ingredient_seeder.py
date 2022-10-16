from flask_seeder import Seeder, Faker, generator

from app.repositories.models import Ingredient
from app.seeds.utils.generator_extension import ListSequence
from app.seeds.base_seeder import BaseSeeder


class IngredientTemplate(BaseSeeder):

    possible_items = [
        'Tomato', 'Bacon', 'Pepperoni', 'Corn', 'Meat', 'Mushrooms',
        'Pinnapple', 'Onion', 'Cheese', 'Spinach', 'Anchovies', 'Garlic'
        ]

    def generate_info(self) -> None:
        faker = Faker(
            cls=Ingredient,
            init={
                "_id": generator.Sequence(end=len(self.possible_items)),
                "name": ListSequence(self.possible_items),
                "price": generator.Integer(start=1, end=4)
            }
        )
        self.faker = faker


class IngredientSeeder(IngredientTemplate, Seeder):

    def run(self):
        self.template_seed()
