x=int(input("Enter the limit:"))
print(f"Enter {x} Elements:")
a=[]
for i in range(0,x):
    a.append(int(input()))
for i in range(0,x):
    print(a[i]*a[i])
