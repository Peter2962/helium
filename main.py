import os
from flask import Flask
from database import db
from dotenv import load_dotenv
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

## Resources ##
from resources.Base import Base
from resources.auth.Login import Login
from resources.auth.Register import Register
## End Resources ##

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + os.getenv('MYSQL_USERNAME') + ':' + os.getenv('MYSQL_PASSWORD') + '@' + os.getenv('MYSQL_HOST') + '/' + os.getenv('MYSQL_DATABASE')

def main():
	db.init_app(app)
	## Models ##
	import models.User
	## End Models ##

	with app.app_context():
		db.drop_all()
		db.create_all()

	app.run(debug=True)


api.add_resource(Base, '/')
api.add_resource(Login, '/sign-in')
api.add_resource(Register, '/sign-up')


if __name__ == '__main__':
	main()