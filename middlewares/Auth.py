from utils.auth import auth_check
from flask import jsonify, request
from flask_http_middleware import BaseHTTPMiddleware
from config import public_routes, ignored_routes, jwt_identifier

class Auth(BaseHTTPMiddleware):
	def __init__(self):
		super().__init__()

	def dispatch(self, request, call_next):
		isAuthenticated = False
		if request.path in public_routes:
			return jsonify({'message': 'unauthenticated'})
		elif request.path in ignored_routes:
			return call_next(request)

		if auth_check():
			isAuthenticated = True

		if isAuthenticated == True:
			return call_next(request)
		else:
			return jsonify({'message': 'unauthenticated'})