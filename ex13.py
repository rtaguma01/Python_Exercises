#Exercise 13: Parameters, Unpacking, Variables

from sys import argv

script, first, second, third = argv

print "The script is called: ", script
print "Your first variable is: ", first
print "Your second variable is: ", second
print "Your third variable is: ", third
dinner = raw_input("What did you eat for dinner?")
lunch = raw_input("What did you eat for lunch?")

print "You ate %s for dinner and %s for lunch?" %(
dinner, lunch)