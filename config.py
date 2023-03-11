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
# routes_mapping = {
# 	'/': {
# 		'action': 'BaseController.sendPing',
# 		'method': 'GET'
# 	},
# 	'/auth/sign-in': {
# 		'action': 'AuthController.signIn'
# 	},
# 	'/auth/sign-up': {
# 		'action': 'AuthController.signUp'
# 	}
# }

routes_mapping = [
	{
		'path': '/',
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

# list of moderls to import
models = [
	'User'
]

# name of the jwt field included in the header
jwt_identifier = '_token'