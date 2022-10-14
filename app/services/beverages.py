from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, request

from ..controllers import BeverageController
from ..common.utils import response_builder

beverage = Blueprint('beverage', __name__)


@beverage.route('/', methods=POST)
def create_beverage():
    response = BeverageController.create(request.json)
    return response_builder(response)
