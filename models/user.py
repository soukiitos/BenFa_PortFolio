from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.integer, primary_key=True)
    username = db.Column(db.string(255), unique=True, nullable=False)
    email = db.Column(db.string(255), unique=True, nullable=False)
    password = db.Column(db.string(255), nullable=False)
    First_name = db.Column(db.string(255))
    last_name = db.Column(db.string(255))
    address = db.Column(db.string(255))
    role = db.Column(db.string(25), default='seller' 'buyer')