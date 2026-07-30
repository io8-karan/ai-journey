from enum import Enum
class Status(Enum):
    ORDERED_PLACED=1
    PACKED=2
    SHIPPED=3
    OUT_FOR_DELIVERY=4
    DELIVERED=5
    CANCELLED=6