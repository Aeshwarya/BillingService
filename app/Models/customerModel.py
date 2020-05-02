class customerModel:

    def __init__(self, customer_id , name):
        self.customer_id = customer_id
        self.name = name

    def generate_response_format(self):
        customer_details = {}
        customer_details["name"] = self.name
        return customer_details

