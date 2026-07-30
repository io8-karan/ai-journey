from customer import Customer
from package import Package
from tracking import Order,Order_Manager
from reports import Report
from validators import Validation
import time

def menu():
    print("\n" + "=" * 50)
    print("      SMART PACKAGE TRACKING SYSTEM")
    print("=" * 50)
    print("1. Add Package")
    print("2. Search Package")
    print("3. Update Package Status")
    print("4. Reports")
    print("5. Exit")
    print("=" * 50)

tracking=Order_Manager()
reports=Report(tracking)
while True:
    menu()
    
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print("Add Package")
        name=input("Enter Your Name=")
        phone_no=input("Enter your Phone Number=")
        email=input("Enter Your Email=")
        address=input("Enter Your Address=")
        customer=Customer(name,phone_no,email,address)
        package=Package(customer,"Ludhiana")
        validate=Validation(customer,package)
        track=Order(customer,package)
        if validate.validate_email() and validate.validate_phone_no():
             print("Valid Email and Phone No")
             tracking.create_order(track)
             tracking.save_order(track)
             time.sleep(1)
             print(" order saved")
        else:
             print("Invalid Email and phone number")
       
    elif choice == "2":
        print("Search Package")
        validate.validate_tracking_id()
        tracking.search_order()
    elif choice == "3":
        print("Update Package Status")
        validate.validate_tracking_id()
        tracking.update_status()
        tracking.save_order()
    elif choice == "4":
        print("Reports")
        reports.count_today_order()
        reports.count_delivered_order()
        reports.count_pending_order()
        reports.count_cancelled_order()
        reports.group_orders_by_status()
    elif choice == "5":
        print("Thank you for using Smart Package Tracking System!")
        break

    else:
        print("Invalid Choice! Please enter a number between 1 and 5.")