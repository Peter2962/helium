from database import db
from models.user import User
from flask import jsonify, request
from utils.auth import encode_token, decode_token, hash_password

class AuthController():
	def __init__(self):
		pass

	def signIn():
		return jsonify({'res': 'signin'})

	def signUp():
		return jsonify({'res': 'signup'})