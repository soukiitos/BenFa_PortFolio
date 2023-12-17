from extensions import db
# The payment class

class Payment(db.Model):
    card_number = db.Column(db.String(16), primary_key=True)
    username = db.Column(db.String(255), db.ForeignKey('user.username'), nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('order.order_id'), nullable=False)
    payment_method = db.Column(db.String(50))
    expiration = db.Column(db.String(5))
    security_code = db.Column(db.String(3)) 