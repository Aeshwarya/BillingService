from .baseService import BaseService
from ..DmModels.receipt import Receipt
from ..DmModels import db
from ..Models import receiptDetails
from ..Models.receiptDetails import receiptDetails
from ..Models.responseStatus import reseponseStatus

class receiptService(BaseService):

    def add_receipt(self, bill_details, data):
        print("bill_details", bill_details)
        platform_id = data['platformBillID']
        tran_id = data['paymentDetails']['platformTransactionRefID']
        payment_id = data['paymentDetails']['uniquePaymentRefID']
        with self.app.app_context():
            new_receipt = Receipt(bill_id=bill_details.id, platform_id= platform_id, transaction_id = tran_id, payment_id = payment_id , amount = bill_details.amount, bill_generated_date = bill_details.date_created)
            print("new receipt", new_receipt)
            db.session.add(new_receipt)
            db.session.commit()
            id = new_receipt.id

        receipt_obj = receiptDetails(id, bill_details.id , platform_id, new_receipt.date_created)
        receipt_details_obj = receipt_obj.generate_receipt()
        response = {}
        response["status"] = reseponseStatus.SUCCESS
        response["message"] = receipt_details_obj

        return response


