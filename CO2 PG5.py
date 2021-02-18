n=int(input("Enter a limit:"))
for i in range(1,n+1):
    for j in range(0,i+1):
        x=i*j
        if x==0:
            continue
        else:
            print(x,end=" ")
    print("\n")

