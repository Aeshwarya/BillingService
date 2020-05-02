from flask import make_response, Blueprint, current_app, jsonify, request
from ..services.billingService import billingService
from ..lib.responseHandler import responseHandler
from app.Models.responseStatus import reseponseStatus
from flask_jwt_extended import (jwt_required)
BillsController = Blueprint('bills_controller', __name__)
billingService = billingService(current_app)

@BillsController.route("/bills/fetch", methods=['POST'])
@jwt_required
def get_bill():
    try:
        data = request.json
        print("data", data)
        mobile_number = data['customerIdentifiers'][0]['attributeValue']
        customer_id = billingService.get_customer_id(mobile_number)
        if customer_id == None:
            response = {"error":"customer not found", "status": reseponseStatus.FALIURE}
        else:
            response = billingService.get_bill_using_customer_id(customer_id)
        print("response", response)
        responseHandlerObj = responseHandler()
        return responseHandlerObj.returnResponse(response)

    except Exception as e:
        return make_response(jsonify({'error': 'Something went wrong in generating bill'}), 400)


@BillsController.route("/bills/add", methods=['POST'])
def add_bill():
    try:
        data = request.json
        print("data", data)
        mobile_number = data['mobile_number']
        bill_amount = data['amount']
        customer_id = billingService.get_customer_id(mobile_number)
        bill_id = billingService.add_bill(customer_id, bill_amount)
        return make_response(jsonify({'message': 'bill added', "bill_id": bill_id }), 200)

    except Exception as e:
        print(e)
        return make_response(jsonify({'message': 'Something went wrong in generating bill'}), 200)

@BillsController.route("/customer", methods=['PUT'])
def add_customer():
    try:
        data = request.json
        print("data", data)
        mobile_number = data['mobile_number']
        customer_name = data['name']
        customer_id = billingService.add_customer(customer_name, mobile_number)
        return make_response(jsonify({'message': 'customer added', "customer_id": customer_id }), 200)

    except Exception as e:
        print(e)
        return make_response(jsonify({'message': 'Something went wrong in generating bill'}), 200)
