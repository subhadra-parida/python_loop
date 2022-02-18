a=int(input("enter any number="))
i=0
rev=0
while a>0:
    i=a%10
    rev=(rev*10+i)
    a=a//10
print(rev,"is the reverse number")
