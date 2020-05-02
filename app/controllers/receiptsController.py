from flask import make_response, Blueprint, current_app, jsonify, request
from ..services.receiptService import receiptService
from ..services.billingService import billingService
from ..lib.responseHandler import responseHandler
from app.Models.responseStatus import reseponseStatus
from flask_jwt_extended import (jwt_required)
billingService = billingService(current_app)
receiptService = receiptService(current_app)
ReceiptsController = Blueprint('receipts_controller', __name__)

@ReceiptsController.route("/bills/fetchReceipt", methods=['POST'])
@jwt_required
def get_receipt():
    try:
        data = request.json
        print("data", data)
        bill_details = billingService.get_bill_using_bill_id(data['billerBillID'])
        print("bill_details", bill_details)
        if bill_details == None:
            response = {"error": "bill not found", "status": reseponseStatus.FALIURE}
        else:
            amount_paid = data["paymentDetails"]["amountPaid"]["value"]
            print(amount_paid, bill_details.amount)
            if amount_paid != bill_details.amount:
                response = {"error": "incorrect amount", "status": reseponseStatus.FALIURE}
            else:
                response = receiptService.add_receipt(bill_details, data)
        print("response", response)
        responseHandlerObj = responseHandler()
        return responseHandlerObj.returnResponse(response)

    except Exception as e:
        print(e)
        return make_response(jsonify({'message': 'Something went wrong in generating receipts'}), 200)
