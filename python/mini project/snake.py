# Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" where players use hand gestures to represent a snake, water, or a gun. The gun beats the snake, the water beats the gun, and the snake beats the water.
# Write a python program to create a Snake Water Gun game in Python using if-else statements. Do not create any fancy GUI. Use proper functions to check for win.

import random as r
print("Snake, Water and Gun is a variation of the children's game 'rock-paper-scissors' where players use hand")
print("gestures to represent a snake, water, or a gun. The gun beats the snake, the water beats the gun, and the")
print("snake beats the water.")
print("0 denote snake, 1 donate water, 2 donate gun ")

def winner(a,b):
   
    
    if  a<0 or a>2:
        print("NOt a valid input , choose agian between 0 to 2")
        return "Invalid Input"

    elif a == b:
        return "Draw the match"
    elif  a==0 and b==1 or a==1 and b==2 or a==2 and b==0:
        return "user win "   
    else:
       return "computer win " 
    


while True :
   try:
        choice=int(input("Enter a choice(1 for start the game ,2 for end the game=)"))
        if choice == 1:
          user=int(input("user choose  a no. from 0 to 2="))
     
          rando=r.randint(0,2)
          print("computer choice=",rando)
          win=winner(user,rando)

          if win == "Invalid Input":  
           continue
          print(win)
        elif choice == 2:
         print("exit game")
         break
        else:
         print("Invalid Choice")
         break
   except ValueError:
      print("Value Error")
      continue