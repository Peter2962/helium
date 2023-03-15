import os
import importlib
from flask import request
from config import middlewares, routes_mapping, models, jwt_identifier, auth

def map_route(routeName, routeAction):
	pass

def register_middlewares(app):
	for name in os.listdir('middlewares'):
		if name.endswith('.py'):
			middleware = name[:-3]
			middlewareClass = getattr(importlib.import_module('middlewares' + '.' + middleware), middleware)
			app.wsgi_app.add_middleware(middlewareClass)

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