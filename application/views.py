from flask import current_app as app, request, jsonify
from application import models, db


@app.route("/users",  methods=['GET', 'POST'])
def users():
    """
    Представление для демонстрации всех пользователей
    и создания нового пользователя
    """
    if request.method == 'GET':
        result = []
        for user in models.User.query.all():
            result.append(user.to_dict())
        return jsonify(result)
    elif request.method == 'POST':
        user_data = request.json
        new_user = models.User(**user_data)
        db.session.add(new_user)
        db.session.commit()


@app.route("/users/<int:user_id>", methods=['GET', 'PUT', 'DELETE'])
def get_one_user(user_id):
    """
    Представление для демонстрации, редактирования и удаления
    данных пользователя с указанным индексом
    """
    if request.method == 'GET':
        user = models.User.query.get(user_id)
        return jsonify(user.to_dict())

    elif request.method == 'PUT':
        user_data = request.json
        user = models.User.query.get(user_id)
        user.first_name = user_data['first_name']
        user.last_name = user_data['last_name']
        user.age = user_data['age']
        user.email = user_data['email']
        user.role = user_data['role']
        user.phone = user_data['phone']

        db.session.add(user)
        db.session.commit()

    elif request.method == 'DELETE':
        user = models.User.query.get(user_id)
        db.session.delete(user)
        db.session.commit()


@app.route("/orders",  methods=['GET', 'POST'])
def orders():
    """
    Представление для демонстрации всех заказов
    и создания нового заказа
    """
    if request.method == 'GET':
        result = []
        for order in models.Order.query.all():
            result.append(order.to_dict())
        return jsonify(result)
    elif request.method == 'POST':
        order_data = request.json
        new_order = models.Order(**order_data)
        db.session.add(new_order)
        db.session.commit()


@app.route("/orders/<int:order_id>", methods=['GET', 'PUT', 'DELETE'])
def get_one_order(order_id):
    """
    Представление для демонстрации, редактирования и удаления
    данных заказа с указанным индексом
    """
    if request.method == 'GET':
        order = models.Order.query.get(order_id)
        return jsonify(order.to_dict())

    elif request.method == 'PUT':
        order_data = request.json
        order = models.Order.query.get(order_id)
        order.name = order_data['name']
        order.description = order_data['description']
        order.start_date = order_data['start_date']
        order.end_date = order_data['end_date']
        order.address = order_data['address']
        order.price = order_data['price']
        order.customer_id = order_data['customer_id']
        order.executor_id = order_data['executor_id']

        db.session.add(order)
        db.session.commit()

    elif request.method == 'DELETE':
        order = models.Order.query.get(order_id)
        db.session.delete(order)
        db.session.commit()


@app.route("/offers",  methods=['GET', 'POST'])
def offers():
    """
    Представление для демонстрации всех предложений
    и создания нового предложения
    """
    if request.method == 'GET':
        result = []
        for offer in models.Offer.query.all():
            result.append(offer.to_dict())
        return jsonify(result)
    elif request.method == 'POST':
        offer_data = request.json
        new_offer = models.Offer(**offer_data)
        db.session.add(new_offer)
        db.session.commit()


@app.route("/offers/<int:offer_id>", methods=['GET', 'PUT', 'DELETE'])
def get_one_offer(offer_id):
    """
    Представление для демонстрации, редактирования и удаления
    данных предложения с указанным индексом
    """
    if request.method == 'GET':
        offer = models.Offer.query.get(offer_id)
        return jsonify(offer.to_dict())

    elif request.method == 'PUT':
        offer_data = request.json
        offer = models.Offer.query.get(offer_id)
        offer.name = offer_data['name']
        offer.description = offer_data['description']

        db.session.add(offer)
        db.session.commit()

    elif request.method == 'DELETE':
        offer = models.Offer.query.get(offer_id)
        db.session.delete(offer)
        db.session.commit()
