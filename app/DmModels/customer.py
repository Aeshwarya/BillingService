from .base import db, Base

class Customer(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_created = db.Column(db.DateTime,  default=db.func.current_timestamp())
    mobile_number = db.Column(db.String(80), unique=True, nullable=False)
    customer_name = db.Column(db.String(80), unique=False, nullable=False)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_mobile_number(cls, mobile_number):
        return cls.query.filter_by(mobile_number=mobile_number).first()

