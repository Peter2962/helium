import os
import jwt

def map_route(routeName, routeAction):
	pass

def register_middlewares():
	pass

def jwt_encode(payload):
	return jwt.encode(payload, os.getenv('APP_SECRET'), algorithms=[os.getenv('JWT_ALGO')])

def jwt_decode(token):
	return jwt.decode(token, os.getenv('APP_SECRET'), algorithms=[os.getenv('JWT_ALGO')])