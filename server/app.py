from flask import Flask
from flask_migrate import Migrate

from models import db, Customer, Item, Review 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)


@app.route('/')
def index():
    return '<h1>Flask SQLAlchemy Lab 2</h1>'

@app.route('/customer')
def customer():
    return '<h1>Customer</h1>'

@app.route('/item')
def item():
    return '<h1>Item</h1>'

@app.route('/review')
def review():
    return '<h1>Review</h1>'

@app.get('/customer')
def get_customer():
    return Customer.query.all()


if __name__ == '__main__':
    app.run(port=5555, debug=True)