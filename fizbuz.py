for i in range (1,100,1):
    if (i % 3 == 0 |  i % 5 ==0):
        print("FIZBUZZ")
    elif ( i % 5 ==0):
        print("BUZZ")
    elif(i%3==0 ):
        print("Fizz")
    else:
        print(i)