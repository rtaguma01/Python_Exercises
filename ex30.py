#Exercise 30:  Else and If

people = 30
cars = 40
buses = 15

if cars > people:
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "We can't decide."
	

if buses > cars:
	print "That's too many buses."
elif buses < cars:
	print "Maybe we could take the buses."
else:
	print "We still can't decide."
	
if people > buses:
	print "Alright, let's just take the buses."
else:
	print "Fine, let's stay home then."
	
if people + 10 > cars:
	print "There are a lot of people."
elif people + 10 < cars:
	print "There are a lot of cars."
else:
	print "There are an equal number of people and cars."