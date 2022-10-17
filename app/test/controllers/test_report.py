import pytest

from app.controllers import ReportController, BeverageController, IngredientController, SizeController, OrderController
from app.controllers.base import BaseController
from app.test.utils.functions import get_random_choice, shuffle_list


def __order(ingredients: list, beverages: list, size: dict, client_data: dict):
    ingredients = [ingredient.get('_id') for ingredient in ingredients]
    beverages = [beverage.get('_id') for beverage in beverages]
    size_id = size.get('_id')
    return {
        **client_data,
        'ingredients': ingredients,
        'size_id': size_id,
        'beverages': beverages
    }


def __create_items(items: list, controller: BaseController):
    created_items = []
    for item in items:
        created_item, _ = controller.create(item)
        created_items.append(created_item)
    return created_items


def __create_sizes_beverages_and_ingredients(ingredients: list, sizes: list, beverages: list):
    created_ingredients = __create_items(ingredients, IngredientController)
    created_sizes = __create_items(sizes, SizeController)
    created_beverages = __create_items(beverages, BeverageController)
    return created_sizes if len(created_sizes) > 1 else created_sizes.pop(), created_ingredients, created_beverages


def test_report_gets_the_most_requested_ingredient(app, ingredients, sizes, beverages, client_data):
    created_sizes, created_ingredients, created_beverages = __create_sizes_beverages_and_ingredients(
                                                            ingredients, sizes, beverages)
    created_orders = []
    for _ in range(5):
        order = __order(
                shuffle_list(created_ingredients)[:3],
                shuffle_list(created_beverages)[:3],
                get_random_choice(created_sizes),
                client_data)
        created_order, _ = OrderController.create(order)
        created_orders.append(created_order)
    most_requested_ingredient, _ = ReportController.get_report()
    pytest.assume(most_requested_ingredient.get('most_requested_ingredient') is not None)


def test_report_gets_the_month_with_most_revenue(app, ingredients, sizes, beverages, client_data):
    created_sizes, created_ingredients, created_beverages = __create_sizes_beverages_and_ingredients(
                                                            ingredients, sizes, beverages)
    created_orders = []
    for _ in range(5):
        order = __order(
                shuffle_list(created_ingredients)[:3],
                shuffle_list(created_beverages)[:3],
                get_random_choice(created_sizes),
                client_data)
        created_order, _ = OrderController.create(order)
        created_orders.append(created_order)
    most_requested_ingredient, _ = ReportController.get_report()
    pytest.assume(most_requested_ingredient.get('month_with_most_revenue') is not None)


def test_report_gets_top_clients(app, ingredients, sizes, beverages, client_data):
    created_sizes, created_ingredients, created_beverages = __create_sizes_beverages_and_ingredients(
                                                            ingredients, sizes, beverages)
    created_orders = []
    for _ in range(5):
        order = __order(
                shuffle_list(created_ingredients)[:3],
                shuffle_list(created_beverages)[:3],
                get_random_choice(created_sizes),
                client_data)
        created_order, _ = OrderController.create(order)
        created_orders.append(created_order)
    most_requested_ingredient, _ = ReportController.get_report()
    pytest.assume(most_requested_ingredient.get('top_clients') is not None)
