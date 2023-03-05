middlewares = [
	'CheckIfAuthenticated'
]

# list of routes that do not require a valid token but will
# a response if the jwt is not valid
public_routes = [
	'/',
]

# list of routes that the jwt validator will ignore i.e won't send a response to
ignored_routes = [
	'/auth/sign-in',
	'/auth/sign-up'
]

routes_mapping = {
	"/": "BaseController.sendPing",
	"sign-in": "AuthController.signIn",
	'sign-up': 'AuthController.signUp'
}