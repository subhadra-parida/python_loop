num=int(input("enter any number"))
num2=num
sum=0
while num2>0:
	rem=num2%10
	sum=sum+rem
	num2=int(num2/10)
if num%sum==0:
	print(num,"is a harshad number")
else:
	print(num,"is not a harshad number")