# wapp to read 3 nos and find max of 3

n1= float(input("enter first number"))
n2= float(input("enter second number"))
n3= float(input("enter third number"))
if n1 > n2 :
	res = n1
else:
	res = n2
if n3 > res :
	res = n3
print("res =", res)

print (max ( n1,n2,n3), "is max")