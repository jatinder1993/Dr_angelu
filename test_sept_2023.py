

class Load:
    def __init__(self, invoice, price, start_odo, end_odo, broker):
        self.invoice = invoice
        self.price = float(price)
        self.start_odo = int(start_odo)
        self.end_odo = int(end_odo)
        self.broker = broker

    def store_entry(self, entry_data):
        entry_data.append([self.invoice, self.price, self.start_odo, self.end_odo, self.broker])



Load_instance = Load()

load_entry_data = []

Load_instance.store_entry(load_entry_data)

print(load_entry_data)