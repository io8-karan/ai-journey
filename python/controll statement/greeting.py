'''Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. Your program should use time module to get the current hour. Here is a sample program and documentation link for you:
```python 
'''
import time
hour=int(time.strftime("%H"))
if  hour>=1 and hour<12:
    print("Good Morning")
elif hour>=12 and hour<16:
    print("Good Aternoon")
elif hour>=16 and hour<19:
    print("Good Evening ")
else:
    print("Good night")
