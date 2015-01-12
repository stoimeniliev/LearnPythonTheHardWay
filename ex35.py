from sys import exit

def gold_room():
	print "This room is full of gold. How much do you take?"
	
	choice = int(raw_input("> "))
	if choice == 0 or choice == 1 or choice == 2:
		how_much = choice
	else:
		dead("Man, llearn to type a number.")
		
	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
		dead("Upu greedy bastard!")
		
def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honeys."
	print "The fat bear is in front of another door."
	print "How are you ging to move the bear?"
	print "choose between \"taunt bear\" , \"take money\" and \"open door\""
	bear_moved = False
	
	while True:
		choice = raw_input("> ")
		
		if choice == "take money":
			dead("The bear looks at you then slaps your face off.")
		elif choice == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through it now"
			bear_moved = True
		elif choice == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif choice == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means."
			
def cthulhu_room():
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"
	
	choice = raw_input("> ")
	
	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("well that was tasty")
	else:
		cthulhu_room()
		
		
def forward_room():
	print "Muahahah, you decided to continue forward"
	print "Do you know what that means?"
	print "there's never going back again... unless you go back now!"
	print "You can get back now.. or continue forward and never get back...ever..again"
	print "Chooce \"back\" or \"forward\""
	
	choice = raw_input("> ")
	
	if "back" in choice:
		start()
	elif "forward" in choice:
		new_room()
	else:
		dead("Wrong choice, you are now dead")
		
def new_room():
	print "Welcome to the Dying Woods"
	print "They are full of elves and monsters"
	print "You have a couple of choices"
	print "Go to the pave road or start climbing the mountains"
	print "Chooce \"road\" or \"mountain\""
	
	choice = raw_input("> ")
	
	if "road" in choice:
		woods_room()
	elif "mountain" in choice:
		mountain_room()   #da napisha mountain room
	else:
		dead("Wrong choice, you are now dead")
		
		
def woods_room():
	print "You had such a luck"
	print "Nothing happened to you on the road"
	print "You have to choose which to take."
	print "Go inside the Castle or in the forrest to the elves"
	print "Chooce \"Castle\" or \"Forrest\""
	
	choice = raw_input("> ")
	
	if "castle" in choice:
		castle() #da naisha funkciq za zamak
	elif "forrest" in choice:
		forrest_room()  #da napisha funkciq za forrest
	else:
		dead("Wrong choice, you are now dead")
		
		
def forrest():
	print "You win"
	
def castle():
	print "Yes madafaka"
	
def dead(why):
	print why, "Good job!"
	exit(0)
	
def start():
	print "You are in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take?"
	print "Type \"left\" or \"right\" pr \"forward\""
	
	choice = raw_input("> ")
	
	if choice == "left":
		bear_room()
	elif choice == "right":
		cthulhu_room()
	elif choice == "forward":
		forward_room()
	else:
		dead("you stumble around theroom until you startve.")
		
start()