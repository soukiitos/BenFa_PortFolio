from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from extensions import db
from models.user import User
from models.order import Order
from models.product import Product
from models.payment import Payment
import os

app = Flask(__name__)

# Configuration for Flask-SQLAlchemy with MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://benfa:kiitos@localhost/benfa_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the db instance with the app
db.init_app(app)

# Create tables in db
with app.app_context():
    db.create_all()

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/auth', methods=['GET'])
def log_user():
    return render_template('login.html')

@app.route('/payment', methods=['GET'])
def auth_user():
    return render_template('payment.html')

@app.route('/api/orders', methods=['POST'])
def create_order():
    return render_template('order.html')

@app.route('/api/products', methods=['GET'])
def all_products():
    products = Product.query.all()
    return jsonify([product.__dict__ for product in products])
@app.route('/about')
def about():
    return "This application is about BenFa e-commerce"

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