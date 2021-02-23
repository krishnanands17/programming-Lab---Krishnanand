n=int(input("Enter the number:"))
print(f"Factor of {n} are:")
for x in range(0,n):
    for y in range(0,n):
        if(x*y)==n:
            print(x,y)
