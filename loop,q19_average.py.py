i=1
average=0
sum=0
while 1<=10:
    num=int(input("enter any number="))
    sum=sum+num
    print(sum)
    i=i+1
average=sum/10
print(average)
if average%5==0:
    print("divisible")
else:
    print("not")
