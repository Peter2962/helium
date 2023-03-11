import os
import jwt
import importlib
from flask import request
from config import middlewares, routes_mapping, models, jwt_identifier

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
	for route_object in routes_mapping:
		path = route_object['path']
		action = route_object['resource'].split('.')
		controller = action[0]
		method = action[1]
		request_verb = route_object['method']

		# import the controller dynamically
		controllerClass = getattr(
			importlib.import_module(
				'controllers' + '.' + controller
			),
			controller
		)

		app.add_url_rule(
			path,
			methods=[request_verb],
			view_func=getattr(controllerClass, method)
		)

def register_models():
	for model in models:
		importlib.import_module('models' + '.' + model)

def auth_check():
	is_authenticated = False
	jwt_identifier_value = request.headers.get(jwt_identifier)
	isValidJwt = False
	if jwt_identifier_value:
		decoded_payload = jwt_decode(jwt_identifier_value)

	return False