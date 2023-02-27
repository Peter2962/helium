from database import db

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	firstname = db.Column(db.String(255), nullable=False)
	lastname = db.Column(db.String(255), nullable=False)
	email = db.Column(db.String(255), unique=True, nullable=False)