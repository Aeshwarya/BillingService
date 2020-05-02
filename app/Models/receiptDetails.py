class receiptDetails:

    def __init__(self, receipt_id, bill_id, platform_id, date):

        self.receipt_id = receipt_id
        self.bill_id = bill_id
        self.platform_id = platform_id
        self.date = date


    def generate_receipt(self):

        receipt_details = {}
        receipt_details["billerBillID"] =  self.bill_id
        receipt_details["platformBillID"] = self.platform_id
        payment_details = {}
        payment_details['id'] = self.receipt_id
        payment_details['date'] = self.date
        receipt_details['receipt'] = payment_details
        return receipt_details