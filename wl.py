#while loop function

def while_loop(limit):
	i = 0
	numbers = []
	while i < limit:
		numbers.append(i)
		i = i + 1
	
		print i
		print numbers
	
while_loop(6)
