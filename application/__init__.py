from flask_sqlalchemy import SQLAlchemy
from flask import Flask


db: SQLAlchemy = SQLAlchemy()


def create_app():
    """
    Создает приложение Flask
    """
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JSON_AS_ASCII'] = False

    with app.app_context():
        db.init_app(app)
        from . import views
        db.create_all()
        from . import migrate
        migrate.load_users('data/users.json')
        migrate.load_orders('data/orders.json')
        migrate.load_offers('data/offers.json')

    return app


