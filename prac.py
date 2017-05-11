#practice copying

from sys import argv

script, file_out, file_in = argv

file = open(file_out)
text = file.read()

in_file = open(file_in, 'w')
in_file.write(text)

line1 = raw_input("Where is woodstock? ")
in_file.write("\n")
in_file.write(line1)


