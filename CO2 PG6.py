s=input("Enter a word:")
c=0
for i in s:
    if i==" ":
        continue
    else:
        c+=1
print(c," Characters in "+s)
