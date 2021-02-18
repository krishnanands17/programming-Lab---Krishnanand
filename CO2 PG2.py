n=int(input("Enter a limit:"))
x=0
y=1
z=0
for i in range(0,n):
    z=x+y
    x=y
    y=z
    print(z)

