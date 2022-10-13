from flask import jsonify

from app.controllers.base import BaseController


class BaseResponse:
    def __init__(self, controller: BaseController):
        self.controller = controller

    def send_request(self):
        self.response = (
            self.controller_request if not self.error else {"error": self.error}
        )

    def get_status_code(self):
        self.status_code = 200 if not self.error else 400

    def jsonify_response(self):
        return jsonify(self.response), self.status_code

    def get_jsonify_response(self, request: tuple):
        self.controller_request, self.error = request
        self.receive_response()
        self.get_status_code()
        return self.jsonify_response()
