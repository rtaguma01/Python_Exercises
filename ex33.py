#Exercise 33:While-Loops



def loop( ): 
	i = 0
	numbers = []

	while i < 6:
		print "At the top i is %d" %i
		numbers.insert(0,i)
	
		i = i + 1
	
	print "Numbers now: ", numbers
	print "At the bottom i is %d" %i
	
loop(numbers)
	
	
print "The numbers:"

for num in numbers:
	print num