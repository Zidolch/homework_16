from . import db


class User(db.Model):
    """
    Модель пользователя
    """
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text(200))
    last_name = db.Column(db.Text(200))
    age = db.Column(db.Integer)
    email = db.Column(db.Text(200))
    role = db.Column(db.Text(200))
    phone = db.Column(db.Text(200))

    def to_dict(self):
        """
        Возвращает данные о пользователе в виде словаря
        """
        user_dict = {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "email": self.email,
            "role": self.role,
            "phone": self.phone
        }
        return user_dict


class Order(db.Model):
    """
    Модель заказа
    """
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text(200))
    description = db.Column(db.Text(200))
    start_date = db.Column(db.Text(200))
    end_date = db.Column(db.Text(200))
    address = db.Column(db.Text(200))
    price = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    customer = db.relationship("User", foreign_keys=[customer_id])
    executor = db.relationship("User", foreign_keys=[executor_id])

    def to_dict(self):
        """
        Возвращает данные о заказе в виде словаря
        """
        order_dict = {
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
        return order_dict


class Offer(db.Model):
    """
    Модель предложения
    """
    __tablename__ = 'offer'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    order = db.relationship("Order", foreign_keys=[order_id])
    user = db.relationship("User", foreign_keys=[executor_id])

    def to_dict(self):
        """
        Возвращает данные о предложении в виде словаря
        """
        offer_dict = {
            "id": self.id,
            "order_id": self.order_id,
            "executor_id": self.executor_id
        }
        return offer_dict
