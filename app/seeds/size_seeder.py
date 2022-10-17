from flask_seeder import Seeder, Faker, generator

from app.repositories.models import Size
from app.seeds.utils.generator_extension import ListSequence
from app.seeds.base_seeder import BaseSeeder


class SizeTemplate(BaseSeeder):

    possible_items = [
        'Personal', 'Small', 'Medium', 'Large', 'Familiar', 'Pizzota'
        ]
    number_of_items: int = 6

    def generate_info(self) -> None:
        faker = Faker(
            cls=Size,
            init={
                "_id": generator.Sequence(end=self.number_of_items),
                "name": ListSequence(self.possible_items),
                "price": generator.Integer(start=4, end=13)
            }
        )
        self.faker = faker


class SizeSeeder(SizeTemplate, Seeder):

    def run(self):
        self.template_seed()
