from flask import jsonify
from config import public_routes, ignored_routes
from flask_http_middleware import BaseHTTPMiddleware

class CheckIfAuthenticated(BaseHTTPMiddleware):
	def __init__(self):
		super().__init__()

	def dispatch(self, request, call_next):
		isAuthenticated = False
		if request.path in public_routes:
			return jsonify({'message': 'unauthenticated'})
		if isAuthenticated == True:
			return call_next(request)
		else:
			return jsonify({'message': request.path})