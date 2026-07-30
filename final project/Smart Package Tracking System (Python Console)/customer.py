class Customer:

    def __init__(self, name, phone_no, email, address):
        self.name = name
        self.phone_no = phone_no
        self.email = email
        self.address = address
    def update_email(self, new_email):
        self.email = new_email

    def update_address(self, new_address):
        self.address = new_address

    def display(self):
        print("Customer Detail")
        print(f"Customer Name   = {self.name}")
        print(f"Phone Number    = {self.phone_no}")
        print(f"Email           = {self.email}")
        print(f"Address         = {self.address}")