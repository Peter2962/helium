import os
import jwt
import importlib
from config import middlewares, routes_mapping

def map_route(routeName, routeAction):
	pass

def register_middlewares(app):
	for name in os.listdir('middlewares'):
		if name.endswith('.py'):
			middleware = name[:-3]
			middlewareClass = getattr(importlib.import_module('middlewares' + '.' + middleware), middleware)
			app.wsgi_app.add_middleware(middlewareClass)
	pass

def jwt_encode(payload):
	return jwt.encode(payload, os.getenv('APP_SECRET'), algorithms=[os.getenv('JWT_ALGO')])

def jwt_decode(token):
	return jwt.decode(token, os.getenv('APP_SECRET'), algorithms=[os.getenv('JWT_ALGO')])

def register_routes(app):
	for path in routes_mapping:
		action = routes_mapping[path].split('.')
		controller = action[0]
		method = action[1]

		# import the controller dynamically
		controllerClass = getattr(
			importlib.import_module(
				'controllers' + '.' + controller
			),
			controller
		)

		app.add_url_rule(
			path,
			view_func=getattr(controllerClass, method)
		)

