x=int(input("Enter the limit:"))
print("Enter the Elements")
a=[]
for i in range(0,x):
    a.append(int(input()))
for i in a:
     if i<0:
        continue;
     else:
        print(i)
