from flask_jwt import jwt_required
from flask import render_template
from flask import Response

"""

 Parent Class Controller

"""


class BaseController:
    def __init__(self):
        self.notification = False
