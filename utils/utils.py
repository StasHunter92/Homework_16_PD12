from flask import json

from classes.classes import User, Order, Offer
from config import USERS_PATH, ORDERS_PATH, OFFERS_PATH


def open_json_file(file) -> json:
    """
    Returns loaded JSON file
    :param file: JSON file to open
    """
    with open(file, encoding="utf-8") as file:
        return json.load(file)


def add_users_to_database() -> list:
    """
    Add user object to a list of users
    :return: list of users
    """
    users = open_json_file(USERS_PATH)
    users_list = []
    for user in users:
        user_to_add = User(
            id=user.get("id"),
            first_name=user.get("first_name"),
            last_name=user.get("last_name"),
            age=user.get("age"),
            email=user.get("email"),
            role=user.get("role"),
            phone=user.get("phone")
        )
        users_list.append(user_to_add)
    return users_list


def add_orders_to_database() -> list:
    """
    Add order object to a list of orders
    :return: list of orders
    """
    orders = open_json_file(ORDERS_PATH)
    orders_list = []
    for order in orders:
        order_to_add = Order(
            id=order.get("id"),
            name=order.get("name"),
            description=order.get("description"),
            start_date=order.get("start_date"),
            end_date=order.get("end_date"),
            address=order.get("address"),
            price=order.get("price"),
            customer_id=order.get("customer_id"),
            executor_id=order.get("executor_id")
        )
        orders_list.append(order_to_add)
    return orders_list


def add_offers_to_database() -> list:
    """
    Add offer object to a list of offers
    :return: list of offers
    """
    offers = open_json_file(OFFERS_PATH)
    offers_list = []
    for offer in offers:
        offer_to_add = Offer(
            id=offer.get("id"),
            order_id=offer.get("order_id"),
            executor_id=offer.get("executor_id")
        )
        offers_list.append(offer_to_add)
    return offers_list
