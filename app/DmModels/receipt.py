from .base import db, Base

class Receipt(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    bill_id = db.Column(db.Integer, db.ForeignKey('bills.id'), unique=True, nullable=False)
    platform_id = db.Column(db.String(80), nullable=False)
    transaction_id = db.Column(db.String(80), unique=True, nullable=False)
    payment_id = db.Column(db.String(80), unique=True, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    bill_generated_date = db.Column(db.DateTime, unique=False, nullable=False)
    create_date = db.Column(db.DateTime,  default=db.func.current_timestamp())

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

