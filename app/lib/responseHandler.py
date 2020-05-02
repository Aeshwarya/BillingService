from flask import Flask, make_response, Blueprint, current_app, jsonify, request
from ..Models.responseStatus import reseponseStatus
class responseHandler():

    def __init__(self):
        pass

    def returnResponse(self, response):

        if response["status"] == reseponseStatus.SUCCESS:
            return self.returnSuccessFullResponse(response["message"])
        elif response["status"] == reseponseStatus.NOT_FOUND:
            return self.returnNotFoundResponse(response['error'])
        elif response["status"] == reseponseStatus.BAD_REQUEST:
            return self.returnBadRequestResponse(response['error'])
        elif response["status"] == reseponseStatus.FALIURE:
            return self.returnErrorResponse(response['error'])

    def returnSuccessFullResponse(self, responseMessage):
        return make_response(jsonify({"data": responseMessage, "status":200, "success": True}), 200)

    def returnNotFoundResponse(self, reseponseMessage):
        return make_response(jsonify({"error": reseponseMessage , "status":404, "success": False}), 404)

    def returnErrorResponse(self, reseponseMessage):
        return make_response(jsonify({"error": reseponseMessage , "status":500, "success": False}), 500)

    def returnBadRequestResponse(self, reseponseMessage):
        return make_response(jsonify({"error": reseponseMessage , "status":400, "success": False}), 400)
