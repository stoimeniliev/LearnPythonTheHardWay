print "You enter a dark room with two doors. Do you go through doo1 or door 2?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheese cake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."
	
	bear = raw_input("> ")
	
	if bear == "1":
		print "The bear eats your face off. Good Job!"
		print "...."
		print "...."
		print "...."
		print "But this is not the end! You still have an opportunity to live"
		print "There are many challenges that you have to go through but this will be rewarding!"
		print "If a guy walks into a bar and orders 10 beers. Will he get drunk?"
		print "1.Yes."
		print "2.No"
		print "3.Depends"
		
		decision = raw_input("> ")
		
		if decision == "1":
			print "You survive!!!"
		elif decision == "2":
			print "Badum Tss you dieeeee"
		elif decision == "3":
			print "No luck chump"
		else:
			print "You did not obey me. you dieeeee"
		
	elif bear == "2":
		print "The bear eats your legs off. Good job!"
	else:
		print "Well, doing $s is probably better. Bear runs away." % bear
		
elif door == "2":
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."
	
	insanity = raw_input("> ")
	
	if insanity == "1" or insanity == "2":
		print "Your body survives powered by mind of jello. Good job!"
	else:
		print "The insanity rots your eyes into a pool of much. Good job!"
		
else:
	print "You stumble around and fall on a knife and die. Good job!"