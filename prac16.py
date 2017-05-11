from sys import argv

script, filename = argv

file = open(filename, 'w')
file.truncate()

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

file.write(line1)
file.write("\n")
file.write(line2)
file.write("\n")
file.write(line3)