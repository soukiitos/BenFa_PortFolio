from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, FloatField, TextAreaField, SubmitField, SelectField
from wtforms_components import DateField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileField, FileAllowed

class ProductForm(FlaskForm):
    # ProductForm class
    product_id = HiddenField('Product ID')
    name = StringField('Product Name', validators=[DataRequired()])
    category = StringField('Product Category', validators=[DataRequired()])
    price = FloatField('Product Price', validators=[DataRequired()])
    description = TextAreaField('Product Description', validators=[DataRequired()])
    image = FileField('Product Image', validators=[
        FileAllowed(['jpg', 'png', 'jpeg'], 'Image Only Please!')
        ])
    submit = SubmitField('Add Product')


class OrderForm(FlaskForm):
    # OrderForm class
    order_id = StringField('Order ID')
    user_id = StringField('User ID')
    order_date = DateField('Order Date')
    total_price = FloatField('Total Price')
    product_name = StringField('Product Name')
    quantity = StringField('Quantity')
    submit = SubmitField('Submit Order')


class UserForm(FlaskForm):
    # UserForm class
    user_id = StringField('User ID')
    username = StringField('User Name')
    email = StringField(' User mail')
    password = StringField('Password')
    First_name = StringField('First Name')
    last_name = StringField('Last Name')
    role = SelectField('Role', choices=[('buyer', 'Buyer'), ('seller', 'Seller')])
    
    submit = SubmitField('Submit User')


class PaymentForm(FlaskForm):
    # PaymentForm Class
    card_number = StringField('Card Number', validators=[DataRequired(), Length(min=16, max=16)])
    username = StringField('Username', validators=[DataRequired()])
    order_id = StringField('Order ID', validators=[DataRequired()])
    payment_method = SelectField('Payment Method', choices=[('credit', 'Credit Card'), ('debit', 'Debit Card')], validators=[DataRequired()])
    expiration = StringField('Expiration (MM/YY)', validators=[DataRequired(), Length(min=5, max=5)])
    security_code = StringField('Security Code', validators=[DataRequired(), Length(min=3, max=3)])
