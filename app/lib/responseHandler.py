from flask import Flask, make_response, Blueprint, current_app, jsonify, request
from ..Models.responseStatus import reseponseStatus
class responseHandler():

    def __init__(self):
        pass

    def returnResponse(self, response):

        if response["status"] == reseponseStatus.SUCCESS:
            return self.returnSuccessFullResponse(response["message"])
        else:
            return self.returnFaliureResponse(response['error'])

    def returnSuccessFullResponse(self, responseMessage):
        print("here")
        return make_response(jsonify({"data": responseMessage, "status":200, "success": True}))

    def returnFaliureResponse(self, reseponseMessage):

        return make_response(jsonify({"error": reseponseMessage , "status":404, "success": False}))
