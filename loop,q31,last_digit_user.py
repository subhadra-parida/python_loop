# i=10
# num=int(input("neter any number="))
# while i<=num:
#     if num%i:
#         print(num,"last digit number")
#     else:
#         print(num,"not a digit number")
#     i=i+1


num=int(input("enter any number="))
sum=0
while num>0:
    sum=sum+num%10
    num=num//10
print(sum)

