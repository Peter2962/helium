from flask import jsonify, request

class AuthController():
	def __init__(self):
		pass

	def signIn():
		return jsonify({'res': 'signin'})

	def signUp():
		return jsonify({'res': 'signup'})