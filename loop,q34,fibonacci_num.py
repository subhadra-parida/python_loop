num=int(input("enter any number="))
a=0
b=1
c=a+b
while c<=num:
    print(c)
    a=b
    b=c
    c=a+b
