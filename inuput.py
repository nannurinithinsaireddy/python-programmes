def func():

	a=int(input("first number is"))
	b=int(input("second number is"))
	c=int(input("third number is"))

	if a==b and b==c:
		print("all are same")
	elif a>b and b>c:
		print("a is greater")
	elif a<b and b<c: 
		print("c is greater")
	elif a<b and b>c:
		print("b is greater")
func()