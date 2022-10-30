from flask import Blueprint, request, jsonify

from classes.classes import db, Offer

offers_blueprint = Blueprint('offers_blueprint', __name__)


@offers_blueprint.route('/offers/', methods=['GET', 'POST'])
@offers_blueprint.route('/offers/<int:ofid>', methods=['GET', 'PUT', 'DELETE'])
def get_offers(ofid=None):
    """
    Get all offers or one offer from the database
    :param ofid: id of the offer
    :return: JSON object and status code
    """
    if ofid is None:
        if request.method == 'GET':
            offers = []
            result = Offer.query.all()
            for offer in result:
                offers.append(offer.offer_dict())
            return jsonify(offers), 200

        elif request.method == 'POST':
            offer_data = request.json

            new_offer = Offer(
                id=offer_data.get('id'),
                order_id=offer_data.get('order_id'),
                executor_id=offer_data.get('executor_id')
            )

            db.session.add(new_offer)
            db.session.commit()
            return f"Заказ {offer_data.get('id')} успешно добавлен", 201

    else:
        if request.method == 'GET':
            offer = Offer.query.get(ofid)
            return jsonify(offer.offer_dict()), 200

        elif request.method == 'PUT':
            offer_data = request.json
            offer = Offer.query.get(ofid)

            offer.id = offer_data.get('id')
            offer.order_id = offer_data.get('order_id')
            offer.executor_id = offer_data.get('executor_id')

            db.session.add(offer)
            db.session.commit()
            return f"Заказ {ofid} успешно обновлен", 201

        elif request.method == 'DELETE':
            offer = Offer.query.get(ofid)
            db.session.delete(offer)
            db.session.commit()
            return f"Заказ {ofid} успешно удален", 204
