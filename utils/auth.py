import os
import jwt
from flask import request
from datetime import datetime, timedelta, timezone
from flask_bcrypt import generate_password_hash, check_password_hash
from config import middlewares, routes_mapping, models, jwt_identifier, auth

def hash_password(password):
	return generate_password_hash(password).decode('utf8')

def verify_password(first_password, second_password):
	return check_password_hash(first_password, second_password)

def encode_token(payload_field_value):
	payload = {
		'exp': datetime.now(timezone.utc) + timedelta(days=1),
		auth['payload_field_name']: str(payload_field_value),
	}

	return jwt.encode(payload, os.getenv('APP_SECRET'), algorithm=os.getenv('JWT_ALGO'))

def decode_token(token):
	return jwt.decode(
		token,
		os.getenv('APP_SECRET'),
		algorithms=[os.getenv('JWT_ALGO')],
		options={'require_exp': True}
	)

def auth_check():
	try:
		jwt_identifier_value = request.headers.get(jwt_identifier)
		if jwt_identifier_value:
			decoded_payload = decode_token(jwt_identifier_value)
			auth_model = auth['auth_model']
			payload_field_name = auth['payload_field_name']
			"""
			make sure the 'payload_field_name' exists as a key in
			`decoded_payload` dict
			"""
			if payload_field_name in decoded_payload.keys():
				"""
				query the db using the auth_model set in 'auth' config option
				"""
				find_token_owner = auth_model.query.filter_by(
					**{auth['payload_field_name']: decoded_payload[payload_field_name]}
				).first()

				if find_token_owner:
					return True
	except Exception as e:
		return False
