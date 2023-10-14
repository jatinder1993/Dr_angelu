class Load:
    def __init__(self):
        self.invoice = input("Enter the invoice number:  ")
        self.price = float(input("Enter the Amount in numbers only:  "))
        self.start_odo = int(input("Enter the trip start Odometer:  "))
        self.end_odo = int(input("Enter the end of trip odometer:  "))
        self.broker = input("Enter the name of broker:  ")

    def get_info(self):
        print(f'Invoice {self.invoice}, Price = {self.price}')

Load

