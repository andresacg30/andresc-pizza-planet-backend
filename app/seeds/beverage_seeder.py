from flask_seeder import Seeder, Faker, generator

from app.repositories.models import Beverage
from app.seeds.utils.generator_extension import ListSequence
from app.seeds.base_seeder import BaseSeeder


class BeverageTemplate(BaseSeeder):

    possible_items = [
        'Sprite', 'Orange Juice', 'CocaCola', 'Water', 'Beer', 'Ice Tea',
        'Apple Juice', 'Fanta', 'Dr. Pepper', 'Chocolate Milk', 'Wine'
        ]

    def generate_info(self) -> None:
        faker = Faker(
            cls=Beverage,
            init={
                "_id": generator.Sequence(end=len(self.possible_items)),
                "name": ListSequence(self.possible_items),
                "price": generator.Integer(start=3, end=7)
            }
        )
        self.faker = faker


class BeverageSeeder(BeverageTemplate, Seeder):

    def run(self):
        self.template_seed()
