#prac15c


from sys import argv

script, filename = argv
file = open(filename)
text = file.read()
print text

print "Let's open another file!"
print "Name another file:"
file2 = raw_input(">")
text2 = open(file2)
print text2.read()

print "Let's open the first file again."
print "Enter the name of the first file:"
file3 = raw_input(">")
text3 = open(file3)
print text3.read()

print "Let's open the second file again:"
file4 = raw_input(">")
text4 = open(file4)
print text4.read()
