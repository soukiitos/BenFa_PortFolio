from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from forms import ProductForm, OrderForm, UserForm, PaymentForm
from extensions import db
from models.user import User
from models.order import Order
from models.product import Product
from models.payment import Payment
import os
import secrets

app = Flask(__name__)

# Configuration for Flask-SQLAlchemy with MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://benfa:kiitos@localhost/benfa_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# The secret key of FLASK_WTF
app.config['SECRET_KEY'] = 'acfreds14ssjgd109_x'

# db = SQLAlchemy(app)

# Initialize the db instance with the app
db.init_app(app)

# Create tables in db
with app.app_context():
    db.create_all()

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/auth', methods=['GET', 'POST'])
def log_user():
    form = UserForm()

    if form.validate_on_submit():
        new_user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            role=form.role.data  # Set the role based on the form submission
        )
        
        # Save the new user to the database
        db.session.add(new_user)
        db.session.commit()
        
        
        return render_template('login.html')
    
    return render_template('login.html', form=form)

@app.route('/payment', methods=['GET', 'POST'])
def auth_user():
    form = PaymentForm()

    if form.validate_on_submit():
        card_number = form.card_number.data
        if not is_valid_card_number(card_number):
            flash('Please enter a valid card number.', 'error')
            return render_template('payment.html', form=form)
        # Add a new payment to the database
        new_payment = Payment(
            username=form.username.data,
            card_number=card_number,
            order_id=form.order_id.data,
            payment_method=form.payment_method.data,
            expiration=form.expiration.data,
            security_code=form.security_code.data
        )
        db.session.add(new_payment)
        db.session.commit()

        # Flash a success message
        flash('Payment successfully done!', 'success')

        return redirect(url_for('homepage'))

    return render_template('payment.html')

def is_valid_card_number(card_number):
    # Implement your card number validation logic here
    # For example, check if the card number follows a specific format
    # Return True if valid, False otherwise
    return len(card_number) == 16 and card_number.isdigit()

@app.route('/api/orders', methods=['GET'])
def create_order():
    # Handling post requests
    return render_template('order.html')

@app.route('/api/orders', methods=['POST'])
def get_order():
    # Handling post requests
    return jsonify({"message": "This is a post request for orders"})

#@app.route('/api/items', methods=['GET'])
#def other_order():
    # Handling post requests
    #return render_template('order_items.html')

#@app.route('/api/items', methods=['POST'])
#def get_other_order():
    # Handling post requests
    #return jsonify({"message": "This is a post request for order_items"})

@app.route('/api/items', methods=['GET', 'POST'])
def other_order():
    form = OrderForm()

    if request.method == 'POST' and form.validate_on_submit():
        #Add a new Order to the database
        new_order = Order(
            order_id=form.order_id.data,
            user_id=form.user_id.data,
            order_date=form.order_date.data,
            total_price=form.total_price.data
        )
        db.session.add(new_order)
        db.session.commit()

        # Fetch all Orders
        orders = Order.query.all()

        return render_template('order_items.html', orders=orders, form=form)

    # Return a template for the GET request
    return render_template('order_items.html', form=form)

# @app.route('/api/products', methods=['GET'])
#def all_products():
    # Handling post requests
    #return render_template('products.html')

#@app.route('/api/products', methods=['POST'])
#def get_products():
    # Handling get requests
    #products = Product.query.all()
    #return jsonify([product.__dict__ for product in products])

@app.route('/api/products', methods=['GET', 'POST'])
def all_products():
    form = ProductForm()

    if request.method == 'POST' and form.validate_on_submit():
        # Add a new product to the database
        new_product = Product(
            name=form.name.data,
            category=form.category.data,
            price=form.price.data,
            description=form.description.data
        )
        db.session.add(new_product)
        db.session.commit()

        # Return the new product as JSON
        return jsonify({
            'name': new_product.name,
            'category': new_product.category,
            'price': new_product.price,
            'description': new_product.description
        })

    # Fetch all products
    products = Product.query.all()

    return render_template('product.html', products=products, form=form)

    
@app.route('/about')
def about():
    return render_template('about.html')
    # return "This application is about BenFa e-commerce"


@app.route('/more')
def more_details():
    return render_template('More_Details.html')

@app.route('/Be/<text>', strict_slashes=False)
def cisfun(text):
    """display “Be ” followed by the value of the text variable"""
    return 'BenFa ' + text.replace('_', ' ')


@app.route('/BenFa', strict_slashes=False)
@app.route('/BenFa/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """display “BenFa ”, followed by the value of the text variable"""
    return 'BenFa ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def imanumber(n):
    """display “n is a number” only if n is an integer"""
    return "{:d} is a product number".format(n)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    # Uploading users profile pictures
    if request.method == 'GET':
        # Handle GET request
        return render_template('upload.html')
    elif request.method == 'POST':
        # Handle POST request
        uploaded_file = request.files['profile-picture']
        if uploaded_file:
            uploaded_folder = 'uploads'
            if not os.path.exists(uploaded_folder):
                os.makedirs(uploaded_folder)
            file_path = os.path.join(uploaded_folder, uploaded_file.filename)
            uploaded_file.save(file_path)
            return f"File '{uploaded_file.filename}' uploaded successfully at {file_path}"
        else:
            return "No file uploaded!"

# Serve static files
app.static_folder = 'static'


if __name__ == "__main__":
    app.run()
