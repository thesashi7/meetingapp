from controllers.Controller import Controller


def init_api_routes(api):
   api.add_resource(Controller, '/')
