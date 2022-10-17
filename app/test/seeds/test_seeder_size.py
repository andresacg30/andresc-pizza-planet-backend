import pytest

from app.seeds import SizeTemplate
from app.controllers.size import SizeController


def test_size_seeder_creates_sizes_in_db(app):
    seeder = SizeTemplate()
    data = seeder.data_to_list()
    data_from_seeder = []
    for item in data:
        item = {'name': item.name, 'price': item.price}
        created_size, _ = SizeController.create(item)
        data_from_seeder.append(created_size)
    pytest.assume(len(data) != 0)
    possible_sizes = [
        'Personal', 'Small', 'Medium', 'Large', 'Familiar', 'Pizzota'
        ]
    data_in_db, error = SizeController.get_all()
    pytest.assume(error is None)
    pytest.assume(len(data_in_db) != 0)
    for sizes in data_in_db:
        pytest.assume(sizes['name'] in possible_sizes)
