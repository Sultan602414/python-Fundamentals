import random
x=int(input("ENTER THE NUMBER between 1 and 100: "))
y=int(random.random())
print(y)
if(x==y):
    print("Correct")
if(x>y):
    print("too high")
if(x<y):
    print("too low")

if(x>y | x<y/2):
    print("close")
if(x<y | x>y/2 ):
    print("close")