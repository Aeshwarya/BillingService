from .baseService import BaseService
from ..DmModels.bill import Bills
from ..DmModels.customer import Customer
from ..DmModels import db
from ..Models.billFetchStatus import billFetchStatus
from ..Models.billDetails import billDetails
from ..Models.responseStatus import reseponseStatus
from ..Models.customerModel import customerModel

class billingService(BaseService):

    def get_customer_id(self, mobile_number):
        print("mobile_numer", mobile_number)
        with self.app.app_context():
            return Customer.query.filter_by(mobile_number=mobile_number).first()


    def get_all_customers(self):
        with self.app.app_context():
            return Customer.query.all()

    def add_customer(self, name, mobile_number):
        id = -1
        with self.app.app_context():
            new_customer = Customer(customer_name=name, mobile_number=mobile_number)
            print("new customer", new_customer)
            db.session.add(new_customer)
            db.session.commit()
            id = new_customer.id
        return id

    def add_bill(self, customer_id , amount):
        print("hoooleluy", customer_id, amount)
        with self.app.app_context():
            new_bill = Bills(customer_id=customer_id.id, amount=amount)
            print("new bill", new_bill)
            db.session.add(new_bill)
            db.session.commit()
            id = new_bill.id
        return id

    def get_bill_using_customer_id(self, customer):
        print("customer_id", customer, customer.id)
        with self.app.app_context():
            bill_details =  Bills.query.filter_by(customer_id=customer.id).first()
            details = {}
            customer_obj = customerModel(customer.id , customer.customer_name)
            print("customerobj",customer_obj)
            bill_details_obj = {}
            bill_details_obj["customer"] = customer_obj.generate_response_format()
            print(details, bill_details)
            if bill_details == None:
                details["billFetchStatus"] = billFetchStatus.NO_OUTSTANDING
                details["bills"] = []
            else:
                details["billFetchStatus"] = billFetchStatus.AVAILABLE
                bill_obj = billDetails(bill_details.id, bill_details.amount , bill_details.date_created, bill_details.exactness.name , bill_details.recurrence.name)
                print("bill obj", bill_obj)
                details["bills"] = bill_obj.generate_bill_response_obj()

            bill_details_obj["billDetails"] = details

            response = {}
            response["status"] = reseponseStatus.SUCCESS
            response["message"] = bill_details_obj
        return response


    def get_bill_using_bill_id(self, billing_id):
        with self.app.app_context():
               return Bills.query.filter_by(id=billing_id).first()


