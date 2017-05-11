#Exercise 20:  Functions and Files
#importing argv
from sys import argv

script, input_file = argv
#create function print_all
def print_all(f):
#read contents of file
    print f.read()	
#create function rewind
def rewind(f):
#go to first byte in the file
    f.seek(0)
#create function print_a_line
def print_a_line(line_count, f):
#print line from file with newline
    print line_count, f.readline()
#create file object
current_file = open(input_file)
#print 
print "First Let's print the whole file:\n"
#print_all function will read all the contents of the file
print_all(current_file)

print "Now let's rewind, kind of like a tape."
#calls rewind function to go to 1st byte
rewind(current_file)
print "Let's print three lines:"

current_line = 1
#calls print_a_line function from file object and current line
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1

print_a_line(current_line, current_file)