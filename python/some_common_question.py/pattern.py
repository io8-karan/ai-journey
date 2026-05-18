# reverse pattern

for i in range(6,0,-1):
    print("indexing:",i)
    for j in range(0,i):
        print("*",end=" ")
    print() 

        #forward pattern 

for i in range(1,6):
    for j in range(0,i):
        print("*",end=" ")
    print()  
n = 6

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")

    for k in range(i):
        print("* ", end="")

    print()