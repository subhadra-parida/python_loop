num=int(input("enter any number="))
i=1
while i<=num:
    if (num%9==1):
        print(num,"is a magic number")
        break
    else:
        print(num,"is not a magic number")
    i=i+1

