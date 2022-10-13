from app.common.http_methods import GET, POST
from flask import Blueprint, request

from app.common.utils import response_builder
from ..controllers import OrderController

order = Blueprint('order', __name__)


@order.route('/', methods=POST)
def create_order():
    response = OrderController.create(request.json)
    return response_builder(response)


@order.route('/id/<_id>', methods=GET)
def get_order_by_id(_id: int):
    response = OrderController.get_by_id(_id)
    return response_builder(response)


@order.route('/', methods=GET)
def get_orders():
    response = OrderController.get_all()
    return response_builder(response)
