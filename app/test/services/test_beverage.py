import pytest

from app.test.utils.functions import get_random_string, get_random_price


def test_create_beverage_service(create_beverage):
    beverage = create_beverage.json
    pytest.assume(create_beverage.status.startswith('200'))
