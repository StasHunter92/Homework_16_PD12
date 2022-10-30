from flask import Blueprint, request, jsonify

from classes.classes import db, Order

orders_blueprint = Blueprint('orders_blueprint', __name__)


@orders_blueprint.route('/orders/', methods=['GET', 'POST'])
@orders_blueprint.route('/orders/<int:oid>', methods=['GET', 'PUT', 'DELETE'])
def get_orders(oid=None):
    """
    Get all orders or one order from the database
    :param oid: id of the order
    :return: JSON object and status code
    """
    if oid is None:
        if request.method == 'GET':
            orders = []
            result = Order.query.all()
            for order in result:
                orders.append(order.order_dict())
            return jsonify(orders), 200

        elif request.method == 'POST':
            order_data = request.json

            new_order = Order(
                id=order_data.get('id'),
                name=order_data.get('name'),
                description=order_data.get('description'),
                start_date=order_data.get('start_date'),
                end_date=order_data.get('end_date'),
                address=order_data.get('address'),
                price=order_data.get('price'),
                customer_id=order_data.get('customer_id'),
                executor_id=order_data.get('executor_id')
            )

            db.session.add(new_order)
            db.session.commit()
            return f"Заказ {order_data.get('name')} успешно добавлен", 201

    else:
        if request.method == 'GET':
            order = Order.query.get(oid)
            return jsonify(order.order_dict()), 200

        elif request.method == 'PUT':
            order_data = request.json
            order = Order.query.get(oid)

            order.id = order_data.get('id')
            order.name = order_data.get('name')
            order.description = order_data.get('description')
            order.start_date = order_data.get('start_date')
            order.end_date = order_data.get('end_date')
            order.address = order_data.get('address')
            order.price = order_data.get('price')
            order.customer_id = order_data.get('customer_id')
            order.executor_id = order_data.get('executor_id')

            db.session.add(order)
            db.session.commit()
            return f"Заказ {oid} успешно обновлен", 201

        elif request.method == 'DELETE':
            order = Order.query.get(oid)
            db.session.delete(order)
            db.session.commit()
            return f"Заказ {oid} успешно удален", 204
