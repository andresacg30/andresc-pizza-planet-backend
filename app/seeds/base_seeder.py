from typing import List
from abc import ABC
from flask_seeder import Faker


class BaseSeeder(ABC):

    faker: Faker
    number_of_items: int
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
        for item in self.faker.create(self.number_of_items):
            items_to_add.append(item)
        self.data_to_add = items_to_add

    def insert_data(self, data):
        self.db.session.add_all(data)

    def data_to_list(self):
        self.generate_info()
        self.get_data()
        return self.data_to_add
