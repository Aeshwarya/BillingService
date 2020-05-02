from flask import make_response, Blueprint, current_app, jsonify, request
from ..services.receiptService import receiptService
from ..services.billingService import billingService
from ..lib.responseHandler import responseHandler
from app.Models.responseStatus import reseponseStatus
from flask_jwt_extended import (jwt_required)
billingService = billingService(current_app)
receiptService = receiptService(current_app)
ReceiptsController = Blueprint('receipts_controller', __name__)

def validateData(data):
    try:
        return ( data != None and
            data['billerBillID'] != None and
            data['paymentDetails'] != None and
            data['paymentDetails']['amountPaid'] != None and 
            data['paymentDetails']['amountPaid']['value'] != None and
            data['paymentDetails']['platformTransactionRefID'] != None and
            data['paymentDetails']['uniquePaymentRefID'] != None and
            data['platformBillID'] != None )
    except Exception:
        return False

@ReceiptsController.route("/bills/fetchReceipt", methods=['POST'])
@jwt_required
def get_receipt():
    responseHandlerObj = responseHandler()
    
    try:
        data = request.json

        if not validateData(data):
            return responseHandlerObj.returnResponse({"error": "Bad request. Data not correct", "status": reseponseStatus.BAD_REQUEST})

        bill_details = billingService.get_bill_using_bill_id(data['billerBillID'])

        if bill_details == None:
            response = {"error": "bill not found", "status": reseponseStatus.NOT_FOUND}
        else:
            amount_paid = data["paymentDetails"]["amountPaid"]["value"]
            if amount_paid != bill_details.amount:
                response = {"error": "incorrect amount", "status": reseponseStatus.BAD_REQUEST}
            else:
                response = receiptService.add_receipt(bill_details, data)

        return responseHandlerObj.returnResponse(response)

    except Exception as e:
        print(e)
        return responseHandlerObj.returnResponse({"error": "Something went wrong", "status": reseponseStatus.FALIURE})
