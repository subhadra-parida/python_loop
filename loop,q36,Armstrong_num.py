num=int(input("enter any number"))
sum=0
a=num
while a>0:
	digit=a%10
	sum=digit**3+sum
	a=a//10
if sum==num:
	print(num,"armstrong number")
else:
	print(num,"not an armstrong number")