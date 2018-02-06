from flask_restful import Resource
from flask_jwt import jwt_required
from flask import render_template
from flask import Response

"""

 Parent Class Controller

"""
class Controller(Resource):

    def get(self):
       return Response(render_template('calendar.html'))
