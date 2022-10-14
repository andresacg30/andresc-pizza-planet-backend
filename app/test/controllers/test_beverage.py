import pytest

from app.controllers import BeverageController


def test_create(app, beverage: dict):
    created_beverage, error = BeverageController.create(beverage)

