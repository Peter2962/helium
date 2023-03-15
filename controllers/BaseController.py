from flask import jsonify

class BaseController():
	def __init__(self):
		pass

	def sendPing():
		return jsonify({'res': 'ping'})