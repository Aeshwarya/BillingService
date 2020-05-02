from .billsController import BillsController
from .receiptsController import ReceiptsController

def init_app(app):
    app.register_blueprint(BillsController)
    app.register_blueprint(ReceiptsController)

