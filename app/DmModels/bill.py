from .base import db, Base
import enum

class ExactnessType(enum.Enum):
    EXACT = "EXACT"

class Recurrence(enum.Enum):
    ONE_TIME = "ONE_TIME"

class Bills(Base):

    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), unique=True, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    exactness = db.Column(db.Enum(ExactnessType), default=ExactnessType.EXACT)
    recurrence = db.Column(db.Enum(Recurrence),  default=Recurrence.ONE_TIME)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

