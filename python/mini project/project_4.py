# 1. Hotel has these rooms (use tuple - fixed):
#    ("101", "102", "103", "104", "105")

# 2. Take booked rooms as input from user
#    (store in list)

# 3. Check which rooms are still AVAILABLE
#    (use loop + condition)

# 4. Guest enters their name — reverse it as 
#    a secret booking ID

# 5. Print booking confirmation message
#    (use string formatting)

# 6. Find the guest name that is longest
#    (without max())

# 7. Check if any guest name is a palindrome
room=[]
hotel_room= ("101", "102", "103", "104", "105")
for i in range(len(hotel_room)):
 booked_room=input("enter a booked room")
 room.append(booked_room)
