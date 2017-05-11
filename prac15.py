from sys import argv

#unpack modules
script, filename = argv

#Create variable for file
txt = open(filename)

# Prompt to show contents of file
print "Here are the contents of %r:" %filename

# Print read text in file
print txt.read()

print "Type the filename again:"
file_again = raw_input(">")

#new variable for text file
txt_again = open(file_again)

#print contents of read file
print txt_again.read()