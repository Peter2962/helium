from utils.auth import auth_check
from flask import jsonify, request, make_response
from flask_http_middleware import BaseHTTPMiddleware
from config import public_routes, ignored_routes, jwt_identifier

class Auth(BaseHTTPMiddleware):
	def __init__(self):
		super().__init__()

	def dispatch(self, request, call_next):
		if auth_check():
			return call_next(request)
		else:
			return make_response(jsonify({'message': 'unauthenticated'}), 401)