import os
from flask import Flask
from database import db
from flask_cors import CORS
from flask_restful import Api
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_http_middleware import MiddlewareManager
from utils.common import register_routes, register_middlewares, register_models

load_dotenv()

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + os.getenv('MYSQL_USERNAME') + ':' + os.getenv('MYSQL_PASSWORD') + '@' + os.getenv('MYSQL_HOST') + '/' + os.getenv('MYSQL_DATABASE')
app.wsgi_app = MiddlewareManager(app)
CORS(app)

# -- middlewares --
register_middlewares(app)

# -- routes --
register_routes(app)

def main():
	db.init_app(app)

	# -- models --
	register_models()

	with app.app_context():
		db.drop_all()
		db.create_all()

	app.run(
		host=os.getenv('APP_HOST'),
		port=os.getenv('APP_PORT'),
		debug=True
	)


if __name__ == '__main__':
	main()