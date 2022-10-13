from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, request

from ..controllers import IngredientController
from .base_response import BaseResponse

ingredient = Blueprint('ingredient', __name__)
ingredient_response = BaseResponse(IngredientController)


@ingredient.route('/', methods=POST)
def create_ingredient():
    response = ingredient_response.controller.create(request.json)
    return ingredient_response.get_response(response)


@ingredient.route('/', methods=PUT)
def update_ingredient():
    response = ingredient_response.controller.update(request.json)
    return ingredient_response.get_response(response)


@ingredient.route('/id/<_id>', methods=GET)
def get_ingredient_by_id(_id: int):
    response = ingredient_response.controller.get_by_id(_id)
    return ingredient_response.get_response(response)


@ingredient.route('/', methods=GET)
def get_ingredients():
    response = ingredient_response.controller.get_all()
    return ingredient_response.get_response(response)
