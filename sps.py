import random
l=["r","p","s"]

#take input from user
u=input ("enter your choice")

input from the computer
c=random.choice(l)
print("computer chooses",c)

#compare the user and computer choice
if u==c:
	print("tie")
elif u=="r" and c=="p":
	print("computer wins")
	