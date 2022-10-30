import os

USERS_PATH = os.path.join('data', 'users.json')
ORDERS_PATH = os.path.join('data', 'orders.json')
OFFERS_PATH = os.path.join('data', 'offers.json')
SQLALCHEMY_TRACK_MODIFICATIONS = False
# SQLALCHEMY_DATABASE_URI = "sqlite:///homework16.db"
SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
JSON_AS_ASCII = False
DEBUG = True
JSONIFY_PRETTYPRINT_REGULAR = True
