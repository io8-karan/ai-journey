# electricity bill
bills = 0 
units = int(input("Enter units: "))
if units < 0:
    print("no bill to pay because units cannot be negative.")
elif units <= 100:
    bills = units * 5
    print("bills is", bills)
elif units <= 200:
    bills = ((100 * 5) + (units - 100) * 7)
    print("bill is", bills)
elif units > 200:
    bills = ((100 * 5) + (100 * 7) + (units - 200) * 10)
    print("bill is", bills)

after_gst_applied = bills + (18 * bills / 100)
print("after gst applied bill is", after_gst_applied)
fixed_bill = int(input("Enter fixed bill: "))
total_bill = after_gst_applied + fixed_bill
print("total bill is", total_bill)