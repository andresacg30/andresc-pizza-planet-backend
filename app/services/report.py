from app.common.http_methods import GET
from flask import Blueprint

from app.controllers import ReportController
from app.common.utils import response_builder

report = Blueprint('report', __name__)


@report.route('/', methods=GET)
def get_report():
    response = ReportController.get_report()
    return response_builder(response)
