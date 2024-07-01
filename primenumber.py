x=int(input("ENTER THE NUMBER: "))
count=0
for i in range(1,x):
    if(x%i==0):
        count+=1

if(count<=2):
    print(x," is prime number")
else:
    print(x, " is not a prime number")

