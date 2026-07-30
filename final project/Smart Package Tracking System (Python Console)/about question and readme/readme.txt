Project: Smart Package Tracking System

We'll build this in phases.

Phase 1: Project Setup

Create this folder structure:

tracking_system/
│
├── main.py
├── customer.py
├── package.py
├── tracking.py
├── reports.py
├── validators.py
├── utils.py
├── config.py
│
├── orders.txt
└── history.txt

For now, leave every file empty.

Phase 2: Decide Responsibilities

This is the most important step.

customer.py

Responsible for customer information only.

Customer
--------
name
phone
email
address

Methods
--------
display()
package.py

Responsible for package information.

Package
--------
tracking_id
status
booking_date
expected_delivery
current_location

Methods
--------
update_status()
display_package()
validators.py

Contains only validation functions.

validate_phone()

validate_email()

validate_tracking_id()

Uses:

Regular Expressions
tracking.py

Handles all package operations.

create_order()

search_order()

update_status()

save_order()

load_orders()

Uses:

File Handling
UUID
Datetime
Enum
Generators
Function Caching
reports.py

Generates reports.

Today's Orders

Delivered Orders

Pending Orders

Cancelled Orders

Uses:

Counter
defaultdict
utils.py

Small helper functions.

Example

clear_screen()

press_enter()

read_file_generator()

generate_queue_number()

Uses:

itertools
generators
config.py

Stores constants.

ORDER_FILE = "orders.txt"

HISTORY_FILE = "history.txt"

DATE_FORMAT = "%d-%m-%Y %H:%M"
main.py

Only controls the program.

Main Menu

1 Add Package

2 Search Package

3 Update Status

4 Reports

5 Exit
Phase 3: Features We'll Build
✔ Customer Registration

✔ Package Booking

✔ Tracking

✔ Update Status

✔ Delivery Report

✔ Search

✔ Save to File

✔ Load From File

✔ Tracking History
Phase 4: Where Every Topic Will Be Used
Topic	Where we'll use it
OOP	Customer & Package classes
Regex	Validate email, phone, tracking ID
UUID	Generate tracking IDs
Enum	Package status
Datetime	Booking & expected delivery dates
Collections	Reports (Counter, defaultdict, deque)
Itertools	Queue numbers, driver rotation examples
Generators	Read orders one by one
Function Caching	Cache repeated package searches
Type Hints	All functions and methods
File Handling	Save/load orders and history
Exceptions	Invalid input, missing package, file errors
Development Plan

We won't write everything at once.

We'll build it in this order:

Step 1  Customer Class
        ↓
Step 2  Validators
        ↓
Step 3  Package Class
        ↓
Step 4  Tracking System
        ↓
Step 5  File Handling
        ↓
Step 6  Search
        ↓
Step 7  Reports
        ↓
Step 8  Optimization (Generator + Cache)
        ↓
Step 9  Final Menu