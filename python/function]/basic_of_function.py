def upload():
    return "hello world"
print(upload())
# for print sum of two number 

def sum(a,b):
    return a+b
x=sum(5,6)
print(x)

# check odd or even

def check(a):
    if a%2==0:
        print("even")
    else:
        print("odd")
    return a
print(check(5))

# check odd or even with the return value 

def check(a):
    if a%2==0:
        print("even")
    else:
        print("odd")
    return a
check(5)     

# find square of number

def sqr(a):
    return a*a
print(sqr(6))

# Create a function that takes a name and prints welcome message 

def greeting(name):
    print(f"welcome {name}")
greeting("aman")
# check prime or not
def check_prime(a):
    if a<=1:
        print("not a prime")
    else:
      for i in range(2,a):
       if a%i==0:
        print("not a prime")
        break
      else:
         print("prime")
    return a
print(check_prime(35))