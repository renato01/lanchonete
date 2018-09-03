from app import db 


class User(db.Model):
	__tablename__ = "users"

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String, unique=True)
	password = db.Column(db.String)
	name = db.Column(db.String)
	email = db.Column(db.String, unique=True)

	@property
	def is_authenticated(self):
		return True

	@property
	def is_active(self):
		return True

	@property
	def anonymous(self):
		return False

	def get_it(self):
		return str(self.id)

	def __init__(self, username, password, name, email):
		self.username = username
		self.password = password
		self.name = name
		self.email = email

	def __repr__(self):
		return "<User %r>" % self.username

class Food(db.Model):
	__tablename__ = "foods"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, unique=True)
	price = db.Column(db.Float)

	def __init__(self, name, price):
		self.name = name
		self.price = price

	def __repr__(self):
		return "<Food %r>" % self.name
