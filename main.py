import os
from flask import Flask
from database import db
from flask_restful import Api
from routes import load_routes
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_http_middleware import MiddlewareManager
from functions import register_routes, register_middlewares

load_dotenv()

## Middlewares
from middlewares.CheckIfAuthenticated import CheckIfAuthenticated
## End Middlewares

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + os.getenv('MYSQL_USERNAME') + ':' + os.getenv('MYSQL_PASSWORD') + '@' + os.getenv('MYSQL_HOST') + '/' + os.getenv('MYSQL_DATABASE')
app.wsgi_app = MiddlewareManager(app)

# middlewares
register_middlewares(app)

# -- routes --
load_routes(app)

def main():
	db.init_app(app)
	## Models ##
	import models.User
	## End Models ##

	with app.app_context():
		db.drop_all()
		db.create_all()

	app.run(debug=True)


if __name__ == '__main__':
	main()