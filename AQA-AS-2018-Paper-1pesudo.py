number = 0
while number < 1 or number > 10:
    number = int(input("Enter a postive whole number"))
    if number > 10:
        print("number too large")
    else:
        if number < 1:
            print("Not a postive number")
c = 1
for k in range(0,number-1):
    print(c)
    c = (c*(number-1-k))//(k+1)
        