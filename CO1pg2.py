a=2021
b=int(input("Enter the End Year:"))
if(a<b):
    print("Leap year are:")
    for i in range(a,b):
        if(i % 4 == 0 and i % 100 != 0):
            print(i)
else:
    print("Invalid Year")
