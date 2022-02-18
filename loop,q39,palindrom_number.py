n=int(input("enter any number"))
temp=n
rev=0
while n>0:
	digit=n%10
	rev=rev*10+digit
	n=n//10
if temp==rev:
	print(n,"is a palindrom number")
else:
	print(n,"is not a palindrom number")
    