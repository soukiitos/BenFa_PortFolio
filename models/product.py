from extensions import db

class Product(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    category = db.Column(db.String(255))
    price = db.Column(db.Float)
    description = db.Column(db.Text)