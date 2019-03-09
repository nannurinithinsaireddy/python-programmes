import random

d = 0
p = 0

while true:
		r = input("press r to roll, q to quit : ")

		if r == 'r':
			d = random.randint(1,6)
			print("you got  :" ,d)
			if d == 6:
				print("congratulations, you can paly now ")
				break
			else:
				print("roll again , till you get 6.")

while true:
	r = input("press r to roll,q to quit : ")

	if r== 'r' :
		d = random.randint(1,6)
		print("you got :",d)

		p = p+d
		if p > 100:
				p = p-d
				print("wait till you get", 100-p,"or less .")

				print("your new position is :",p)

		if p== 100:
					print("you won!")
					exit()
		if p==8:
					p = 37
					print("wow, a ladder , go to ",p)
		if  p == 12:
				p = 89 
				print ("wow,a ladder , go to " , p)
		if  p==99:
				p= 10 
				print ("you have been bitten by a snake "," go to ",p)

			   

	elif r == 'q':
					print ("Bye!")
					exit()