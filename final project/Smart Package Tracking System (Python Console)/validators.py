import re
from customer import Customer
from package import Package
class Validation:
 def __init__(self,customer:Customer,package:Package):
   self.customer=customer
   self.package=package
 def validate_email(self) -> bool:
    pattern=r"^[a-z][a-z0-9_]*@[a-z]+\.[a-z]+$"
    return bool(re.fullmatch(pattern, str(self.customer.email)))

 def validate_phone_no(self) -> bool:
    pattern=r"^[0-9]{10}$"
    return bool(re.fullmatch(pattern, str(self.customer.phone_no)))

 def validate_tracking_id(self, tracking_id: str) -> bool:
   pattern=r"^[a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12}$"
   return bool(re.fullmatch(pattern, str(tracking_id)))