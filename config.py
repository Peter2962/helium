from models.user import User

middlewares = [
	'Auth'
]

# list of routes that do not require a valid token but will
# return a response if the jwt is not valid
public_routes = [
	'/',
]

# list of routes that the jwt validator will ignore i.e won't send a response to
ignored_routes = [
	'/auth/sign-in',
	'/auth/sign-up'
]

# routes mapping configuration
routes_mapping = [
	{
		'path': '/api',
		'resource': 'BaseController.sendPing',
		'method': 'GET'
	},
	{
		'path': '/auth/sign-in',
		'resource': 'AuthController.signIn',
		'method': 'POST'
	},
	{
		'path': '/auth/sign-up',
		'resource': 'AuthController.signUp',
		'method': 'POST'
	}
]

# list of models to import
models = [
	'user'
]

"""
name of the jwt field included in the header
"""
jwt_identifier = '_token'

"""
auth configuration
"""
auth = {
	'auth_model': User,
	'payload_field_name': 'id'
}