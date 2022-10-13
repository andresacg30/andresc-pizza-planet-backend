from app.common.http_methods import GET, POST
from flask import Blueprint, request

from app.services.base_response import BaseResponse
from ..controllers import OrderController

order = Blueprint('order', __name__)
order_response = BaseResponse(OrderController)


@order.route('/', methods=POST)
def create_order():
    response = order_response.controller.create(request.json)
    return order_response.get_jsonify_response(response)


@order.route('/id/<_id>', methods=GET)
def get_order_by_id(_id: int):
    response = order_response.controller.get_by_id(_id)
    return order_response.get_jsonify_response(response)


@order.route('/', methods=GET)
def get_orders():
    response = order_response.controller.get_all()
    return order_response.get_jsonify_response(response)
