num=int(input("entwer any number="))
i=0
sum=0
r=0
while num!=0:
    r=num%10
    sum=sum+r*pow(2,i)
    num=num//10
    i=i+1
print(sum)
