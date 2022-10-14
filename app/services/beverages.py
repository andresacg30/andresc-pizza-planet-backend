from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, request

from ..controllers import BeverageController
from ..common.utils import response_builder


beverage = Blueprint('beverage', __name__)


@beverage.route('/', methods=POST)
def create_beverage():
    response = BeverageController.create(request.json)
    return response_builder(response)


@beverage.route('/', methods=PUT)
def update_ingredient():
    response = BeverageController.update(request.json)
    return response_builder(response)


@beverage.route('/id/<_id>', methods=GET)
def get_beverage_by_id(_id: int):
    response = BeverageController.get_by_id(_id)
    return response_builder(response)
