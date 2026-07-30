from customer import Customer
from package import Package
from status import Status
import
class Order:
    def __init__(self,customer:Customer,package:Package):
        self.customer=customer
        self.package=package
    def __str__(self):
         return (
          f"Customer Name: {self.customer.name}\n"
          f"Phone: {self.customer.phone_no}\n"
          f"Email: {self.customer.email}\n"
          f"Tracking ID: {self.package.tracking_id}\n"
          f"Status: {self.package.status.name}\n"
          f"Location: {self.package.current_location}"
    )
       
    def display(self):
                    self.customer.display()
                    self.package.display_package_detail()
class Order_Manager():
          def __init__(self):
              self.orders: list[Order]=[]

          def create_order(self,order:Order):
                self.orders.append(order)
                print(order)

          def search_order(self, trackid: str = None):
                        if trackid is None:
                              trackid = input("Enter a tracking Id=")
                        for track in self.orders:
                              current_id = track.package.tracking_id
                              if trackid == current_id:
                                    print(track)

          def update_status(self, trackid: str = None):
                        if trackid is None:
                              trackid = input("Enter a tracking Id=")
                        for track in self.orders:
                              tracked_id = track.package.tracking_id
                              if trackid == tracked_id:
                                    location = input("Enter You Location=").lower()
                                    track.package.current_location = location
                                    if location == "packing center":
                                          track.package.status = Status.PACKED
                                    elif location == "courier hub":
                                          track.package.status = Status.SHIPPED
                                    elif location == "destination hub":
                                          track.package.status = Status.OUT_FOR_DELIVERY
                                    elif location == "customer address":
                                          track.package.status = Status.DELIVERED
                                    else:
                                          print("Invalid location")

          def save_order(self,order:Order):
            with open(r"C:\Karan\ai journey\final project\Smart Package Tracking System (Python Console)\orders.txt","a")as file:
                       file.write(str(order)+ "\n")
                       file.write("-"*50 +"\n")

          def load_order(self):
               with open(r"C:\Karan\ai journey\final project\Smart Package Tracking System (Python Console)\orders.txt","r") as file:
                    for data in file:
                         print(data)