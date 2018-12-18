class DisplayData:
    def __init__(self):
        self.customer_list = []
        self.month_data = []

    def get_customer_list(self):
        return self.customer_list

    def get_month_data(self):
        return self.month_data

    def set_customer_list(self, new_customer_list=[]):
        self.customer_list = new_customer_list

    def set_month_data(self, new_month_data=[]):
        self.month_data = new_month_data
