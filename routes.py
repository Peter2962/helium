from resources.Base import basePing
from resources.Auth import authLogin, authRegister

def load_routes(app):
	@app.route('/', methods=['GET'], endpoint='ping')
	def ping():
		return basePing()

	@app.route('/auth/sign-in', methods=['POST'], endpoint='auth.login')
	def login():
		return authLogin()

	@app.route('/auth/sign-up', methods=['POST'], endpoint='auth.register')
	def register():
		return authRegister()