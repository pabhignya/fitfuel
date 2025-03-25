from flask import Blueprint

# Create a Blueprint for routes
main = Blueprint('main', __name__)

@main.route('/')
def hello():
    return 'Hi'
