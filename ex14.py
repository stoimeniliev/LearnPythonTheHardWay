from sys import argv

script, user_name, second = argv
prompt = 'Kolegaaaaaa '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of pc do yo have?"
computer = raw_input(prompt)

print "Say booom whatsha saaay:"
second = raw_input(' Hiphopa mi e mnogo po-dobar ot hiphopa ti')

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)