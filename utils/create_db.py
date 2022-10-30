from classes.classes import db
from utils.utils import add_users_to_database, add_orders_to_database, add_offers_to_database


def create_database(app) -> None:
    """
    Create database
    :param app: the application object
    :return: None
    """
    with app.app_context():
        db.drop_all()
        db.create_all()
        db.session.add_all(add_users_to_database())
        db.session.add_all(add_orders_to_database())
        db.session.add_all(add_offers_to_database())
        db.session.commit()
