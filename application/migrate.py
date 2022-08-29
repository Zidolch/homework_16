import json
from . import models, db


def load_data(filename):
    """
    Загружает данные из файла в виде json
    """
    with open(filename, 'r', encoding='utf-8') as file:
        json_data = json.load(file)
    return json_data


def load_users(filename):
    """
    Получает данные о пользователсях
    """
    users = load_data(filename)
    for user in users:
        new_user = models.User(**user)
        db.session.add(new_user)
    db.session.commit()


def load_orders(filename):
    """
    Получает данные о заказах
    """
    orders = load_data(filename)
    for order in orders:
        new_order = models.Order(**order)
        db.session.add(new_order)
    db.session.commit()


def load_offers(filename):
    """
    Получает данные о предложениях
    """
    offers = load_data(filename)
    for offer in offers:
        new_offer = models.Offer(**offer)
        db.session.add(new_offer)
    db.session.commit()
