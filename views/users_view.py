from flask import Blueprint, request, jsonify

from classes.classes import db, User

users_blueprint = Blueprint('users_blueprint', __name__)


@users_blueprint.route('/users/', methods=['GET', 'POST'])
@users_blueprint.route('/users/<int:uid>', methods=['GET', 'PUT', 'DELETE'])
def get_users(uid=None):
    """
    Get all users or one user from the database
    :param uid: id of the user
    :return: JSON object and status code
    """
    if uid is None:
        if request.method == 'GET':
            users = []
            result = User.query.all()
            for user in result:
                users.append(user.user_dict())
            return jsonify(users), 200

        elif request.method == 'POST':
            user_data = request.json

            new_user = User(
                id=user_data.get('id'),
                first_name=user_data.get('first_name'),
                last_name=user_data.get('last_name'),
                age=user_data.get('age'),
                email=user_data.get('email'),
                role=user_data.get('role'),
                phone=user_data.get('phone')
            )

            db.session.add(new_user)
            db.session.commit()
            return f"Пользователь {user_data.get('first_name')} {user_data.get('last_name')} успешно добавлен", 201

    else:
        if request.method == 'GET':
            user = User.query.get(uid)
            return jsonify(user.user_dict()), 200

        elif request.method == 'PUT':
            user_data = request.json
            user = User.query.get(uid)

            user.id = user_data.get('id')
            user.first_name = user_data.get('first_name')
            user.last_name = user_data.get('last_name')
            user.age = user_data.get('age')
            user.email = user_data.get('email')
            user.role = user_data.get('role')
            user.phone = user_data.get('phone')

            db.session.add(user)
            db.session.commit()
            return f"Пользователь {uid} успешно обновлен", 201

        elif request.method == 'DELETE':
            user = User.query.get(uid)
            db.session.delete(user)
            db.session.commit()
            return f"Пользователь {uid} успешно удален", 204
