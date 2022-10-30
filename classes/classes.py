from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """User model for database"""
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    email = db.Column(db.String(40))
    role = db.Column(db.String(20))
    phone = db.Column(db.String(20))

    def user_dict(self) -> dict:
        """Convert user data to dictionary"""
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "email": self.email,
            "role": self.role,
            "phone": self.phone
        }


class Order(db.Model):
    """Order model for database"""
    __tablename__ = "order"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(100))
    start_date = db.Column(db.String(40))
    end_date = db.Column(db.String(40))
    address = db.Column(db.String(100))
    price = db.Column(db.Integer)

    customer_id = db.Column(db.Integer, db.ForeignKey(f"{User.__tablename__}.id"))
    customer = db.relationship("User", foreign_keys=[customer_id])

    executor_id = db.Column(db.Integer, db.ForeignKey(f"{User.__tablename__}.id"))
    executor = db.relationship("User", foreign_keys=[executor_id])

    def order_dict(self) -> dict:
        """Convert order data to dictionary"""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "address": self.address,
            "price": self.price,
            "customer_id": self.customer_id,
            "executor_id": self.executor_id
        }


class Offer(db.Model):
    """Offer moder for database"""
    __tablename__ = "offer"

    id = db.Column(db.Integer, primary_key=True)

    order_id = db.Column(db.Integer, db.ForeignKey(f"{Order.__tablename__}.id"))
    order = db.relationship("Order")

    executor_id = db.Column(db.Integer, db.ForeignKey(f"{User.__tablename__}.id"))
    executor = db.relationship("User")

    def offer_dict(self) -> dict:
        """Convert offer data to dictionary"""
        return {
            "id": self.id,
            "order_id": self.order_id,
            "executor_id": self.executor_id
        }
