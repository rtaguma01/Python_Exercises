#Exercise 14:  Prompting and Passing

from sys import argv

script, user_name, occupation = argv

prompt = '--->'

print "Hi %s the %s, I'm the %s script." %(
user_name, occupation, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" %user_name
likes = raw_input(prompt)
print "What kind of work do you do?"
work = raw_input(prompt)
print "Where do you live?"
lives = raw_input(prompt)
print "What kind of computer do you have?"
computer = raw_input(prompt)
print """
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
You are a %r.
And you have a %r computer. Nice
""" %(likes, lives, work, computer)