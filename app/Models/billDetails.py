class billDetails:

    def __init__(self, bill_id , amount , gen_date, rec="ONE_TIME", exact_ness = "EXACT", ):
        self.bill_id = bill_id
        self.amount = amount
        self.gen_date = gen_date
        self.rec = rec
        self.exact_ness = exact_ness

    def generate_bill_response_obj(self):
        bill_details = {}
        bill_details["billerBillID"] = self.bill_id,
        bill_details["generatedOn"] = self.gen_date,
        bill_details["recurrence"] = self.rec,
        bill_details["amountExactness"] = self.exact_ness,
        bill_details["amount"] = self.amount
        return bill_details