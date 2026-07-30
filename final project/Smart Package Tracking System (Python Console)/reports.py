from datetime import datetime
from tracking import Order_Manager
from package import Package
from status import Status
from collections import Counter,defaultdict

class Report:
    def __init__(self,tracking:Order_Manager):
       self.tracking=tracking
    def count_today_order(self):
      count=0
      for counting in self.tracking.orders:
         if counting.package.booking_date.date() == datetime.now().date():
           count+=1
      print("Today Order Count",count)  
    def count_delivered_order(self):
       count_delivery=0
       for counting in self.tracking.orders:
          if counting.package.status == Status.DELIVERED:
             count_delivery+=1
       print("Total Delivered Orders=",count_delivery)

    def count_pending_order(self):
                 count_pending_delivery=0
                 for counting in self.tracking.orders:
                    if counting.package.status != Status.DELIVERED and counting.package.status !=Status.CANCELLED:
                       count_pending_delivery+=1
                 print("Total Pending Delivery Orders=",count_pending_delivery)

    def count_cancelled_order(self):
           count_cancel_delivery=0
           for counting in self.tracking.orders:
              if counting.package.status == Status.CANCELLED:
                 count_cancel_delivery+=1
           print("Total Cancelled Orders=",count_cancel_delivery)
    def status_summary(self):
        status_name=[]
        for status in self.tracking.orders:
            statuses=status.package.status.name
            status_name.append(statuses)
        couting=Counter(status_name)
        print(couting)
    def group_orders_by_status(self):
        grouping=defaultdict(list)
        for order in self.tracking.orders:
            status=order.package.status
            grouping[status].append(order)