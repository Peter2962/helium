from database import db

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	firstname = db.Column(db.String(255), nullable=False)
	lastname = db.Column(db.String(255), nullable=False)
	email = db.Column(db.String(255), unique=True, nullable=False)
	password = db.Column(db.String(255), nullable=False)

	def __init__(self, **kwargs):
		self.firstname = kwargs.get('firstname')
		self.lastname = kwargs.get('lastname')
		self.email = kwargs.get('email')
		self.password = kwargs.get('password')

	def __repr__(self):
		return '<User {}>'.format(self.firstname)