#Prac15b:  Files

from sys import argv

script, filename = argv

#create file object
file = open(filename)

print "Here are the contents of %r:" %filename
print file.read()

print "Enter filename again:"
file_again = raw_input(">")
open_again = open(file_again)
print open_again.read()
