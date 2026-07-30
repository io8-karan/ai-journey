import uuid
from status import Status
from datetime import datetime,timedelta
import random
from customer import Customer
class Package:
    def __init__(self,customer:Customer,current_location):
        self.customer=customer
        self.tracking_id = str(uuid.uuid4())
        self.status = Status.ORDERED_PLACED
        self.booking_date = datetime.now()
        self.expected_delivery = self.booking_date + timedelta(days=random.randint(1,10))
        self.current_location = current_location

    def display_package_detail(self):
        print("Package Detail")
        self.customer.display()
        print(f"Tracking ID: {self.tracking_id}")
        print(f"Status: {self.status}")
        print(f"Booking Date: {self.booking_date}")
        print(f"Expected Delivery: {self.expected_delivery}")
        print(f"Current Location: {self.current_location}")


