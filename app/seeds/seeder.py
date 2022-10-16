from typing import List
from abc import ABC
from flask_seeder import Seeder, Faker, generator

from app.repositories.models import Ingredient
from app.seeds.generator_extension import ListSequence


class BaseSeeder(ABC):

    faker: Faker
    possible_items: List
    data_to_add: List

    def template_seed(self) -> None:
        self.generate_info()
        self.get_data()
        self.insert_data(self.data_to_add)

    def generate_info(self) -> Faker:
        pass

    def get_data(self) -> List:
        items_to_add = []
        for item in self.faker.create(len(self.possible_items)):
            items_to_add.append(item)
        self.data_to_add = items_to_add

    def insert_data(self, data):
        for item in data:
            self.db.session.add(item)



class IngredientTemplate(BaseSeeder):

    possible_items = ['Tomato', 'Bacon', 'Pepperoni', 'Corn', 'Meat', 'Mushrooms']

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
        return self.data_to_add


class BeverageTemplate(BaseSeeder):

    pass


class BeverageSeeder(IngredientTemplate, Seeder):

    def run(self):
        self.template_seed()
        return self.data_to_add