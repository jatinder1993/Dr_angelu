class Load:
    def __init__(self):
        self.invoice = input("Enter the invoice number:  ")
        self.price = float(input("Enter the Amount in numbers only:  "))
        self.start_odo = int(input("Enter the trip start Odometer:  "))
        self.end_odo = int(input("Enter the end of trip odometer:  "))
        self.broker = input("Enter the name of broker:  ")

    def store_entry(self, entry_data):
        entry_data.append([self.invoice, self.price, self.start_odo, self.end_odo, self.broker])


Load_instance = Load()

load_entry_data = []

Load_instance.store_entry(load_entry_data)

print(load_entry_data)