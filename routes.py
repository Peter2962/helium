from resources.Base import basePing
from resources.Auth import authLogin, authRegister

def load_routes(app):
	@app.route('/', methods=['GET'])
	def ping():
		return basePing()

	@app.route('/auth/sign-in', methods=['POST'])
	def login():
		return authLogin()