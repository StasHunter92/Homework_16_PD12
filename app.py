from flask import Flask

from classes.classes import db
from utils.create_db import create_database

from views.users_view import users_blueprint
from views.orders_view import orders_blueprint
from views.offers_view import offers_blueprint

# Create app instance
app = Flask(__name__)
app.config.from_pyfile("config.py")
db.init_app(app)

# Create database
create_database(app)

# Register blueprint
app.register_blueprint(users_blueprint)
app.register_blueprint(orders_blueprint)
app.register_blueprint(offers_blueprint)


# Error handlers
@app.errorhandler(404)
def error_404(error):
    """Page 404 error"""
    return f"OOPS! Page not found", 404


@app.errorhandler(500)
def error_500(error):
    """Internal server error"""
    return f"OOPS! Server have a problem", 500


if __name__ == '__main__':
    app.run()
