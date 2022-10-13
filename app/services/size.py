from app.common.http_methods import GET, POST, PUT
from app.common.utils import response_builder
from flask import Blueprint, request

from ..controllers import SizeController


size = Blueprint('size', __name__)


@size.route('/', methods=POST)
def create_size():
    response = SizeController.create(request.json)
    return response_builder(response)


@size.route('/', methods=PUT)
def update_size():
    response = SizeController.update(request.json)
    return response_builder(response)


@size.route('/id/<_id>', methods=GET)
def get_size_by_id(_id: int):
    response = SizeController.get_by_id(_id)
    return response_builder(response)


@size.route('/', methods=GET)
def get_sizes():
    response = SizeController.get_all()
    return response_builder(response)
