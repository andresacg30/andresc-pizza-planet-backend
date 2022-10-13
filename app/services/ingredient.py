from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, request

from ..controllers import IngredientController
from ..common.utils import response_builder


ingredient = Blueprint('ingredient', __name__)


@ingredient.route('/', methods=POST)
def create_ingredient():
    response = IngredientController.create(request.json)
    return response_builder(response)


@ingredient.route('/', methods=PUT)
def update_ingredient():
    response = IngredientController.update(request.json)
    return response_builder(response)


@ingredient.route('/id/<_id>', methods=GET)
def get_ingredient_by_id(_id: int):
    response = IngredientController.get_by_id(_id)
    return response_builder(response)


@ingredient.route('/', methods=GET)
def get_ingredients():
    response = IngredientController.get_all()
    return response_builder(response)
