import datetime

class billDetails:

    def __init__(self, bill_id , amount , gen_date, customer_id="abc", rec="ONE_TIME", exact_ness = "EXACT"):
        self.bill_id = bill_id
        self.amount = amount
        self.gen_date = gen_date
        self.rec = rec
        self.exact_ness = exact_ness
        self.customer_id = customer_id

    def generate_bill_response_obj(self):
        bill_details = {}
        bill_details["billerBillID"] = str(self.bill_id)
        bill_details["generatedOn"] = self.gen_date.strftime("%Y-%m-%dT%H:%M:%SZ")
        bill_details["recurrence"] = self.rec
        bill_details["amountExactness"] = self.exact_ness
        bill_details["customerAccount"] = {
            "id": self.customer_id
        }
        bill_details["aggregates"] = {
            "total": {
                "displayName": "Total Outstanding",
                "amount": {
                    "value": self.amount
                }
            }
        }
        return bill_details