#Exercise 32: Loops and Lists

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
names = ['Kurt', 'Robyn', 'Savannah']
dogs = ['Crystal', 'Olivia', 'Blaze', 'Marley']

#this first kind of for-loop goes through a list
for number in the_count:
	print "This is count %d" %number

#same as above
for fruit in fruits:
	print "A fruit of type: %s" %fruit

#also we can go through mixed lists too
#notice we have to use %r since we don't know what's in it
for i in change:
	print "I got %r" %i
	
#we can also build lists, firs start with an empty one
elements = []

#then use the range function to do 0 to 5 counts
for i in range(0, 6):
	print "Adding %d to the list." %i
	
	#append is a function that lists understand
	elements.append(i)
	
#now we can print them out too
for i in elements:
	print "Element was: %d" %i
	
for name in names:
	print "My name is %s." %name
	
for dog in dogs:
	print "%s is my dog." %dog
caterpillars = []
	
for baby in range(10, 20):
	print "We have %d babies." %baby
	
	caterpillars.append(baby)
	
for baby in caterpillars:
	print "There are %d caterpillars." %baby
	
	
	
	
	


