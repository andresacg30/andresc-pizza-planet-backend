from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, request

from ..controllers import SizeController
from .base_response import BaseResponse

size = Blueprint('size', __name__)
size_response = BaseResponse(SizeController)


@size.route('/', methods=POST)
def create_size():
    response = size_response.controller.create(request.json)
    return size_response.get_response(response)


@size.route('/', methods=PUT)
def update_size():
    response = size_response.controller.update(request.json)
    return size_response.get_response(response)


@size.route('/id/<_id>', methods=GET)
def get_size_by_id(_id: int):
    response = size_response.controller.get_by_id(_id)
    return size_response.get_response(response)


@size.route('/', methods=GET)
def get_sizes():
    response = size_response.controller.get_all()
    return size_response.get_response(response)
