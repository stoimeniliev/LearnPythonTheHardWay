from sys import exit

skills = []
weapons = []
picked_class = []
firebolt = 50
Firebolt = 50
sword = 50
axe = 50

print "Hello there, Champion!"
print "Pick a name"
name = raw_input("> ")
print "%s! What a brave name!" % name
	
print "%s, choose a class" % name
print "Pick \"Warrior\" if you don't fear close combat"
print "Or..."
print "Pick \"Mage\" if you want to learn black magic and fight creeps using your magic powers"

def user_class():
	print "\"Mage\" or \"Warrior\"?"
	pick_class = raw_input("> ")

	if pick_class in ('Mage', 'mage'):
		print "%s ,you have choosen wisely" % name
		print "Now, %s, you have to pick a skill" % name
		picked_class.append(pick_class)
		magic_pick()
	if pick_class in ('Warrior', 'warrior'):
		print "Mighty, %s, now you have to pick your weapon" % name
		picked_class.append(pick_class)
		weapon_pick()
	
def magic_pick():
	print "You can learn how to do \"Blizzard\" or \"Firebolt\""
	print "Blizzard is an AOE skill, which damages lots of creeps \n and Firebolt is a long-range fireshot \n which makes tons of damage"
	
	first_skill = raw_input("> ")
	
	if first_skill in ('Blizzard', 'blizzard'):
		print "Blizzard is a good choice. It does 50 cold damage"
		print "This is the first skill you have learned"
		skills.append(first_skill)
		
	if first_skill in ('Firebolt', 'firebolt'):
		print "Firebolt is an amazing magic skill it does 50 fire damage"
		print "You will be using it a lot"
		skills.append(first_skill)

def weapon_pick():
	print "Pick your weapon of choice! You can choose between a \"Sword\" or an \"Axe\""
	
	
	first_weapon = raw_input("> ")
	
	if first_weapon in ('Sword', 'sword'):
		print "Sword is a good choice. It does 50 damage"
		print "This is the first weapon you own"
		skills.append(first_skill)
		
	if first_weapon in ('Axe', 'axe'):
		print "There are many great warriors that use axes to slay their enemies. \n The axe does 50 damage"
		print "You will be using it a lot"
		weapons.append(first_weapon)		
def spawn():
	print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
	for pick_class in picked_class:
		print "You have been spawned in the Fairy Lands of the Grand Witch Mountain"
		print "These fields have seen some of the best magicians in the world"
		witch_mountain()
	for pick_class in picked_class:
		print "You have been spawned in the Black Metal Mountains of Northernland"
		print "Some of the greatest Champions have been born here"
		
def witch_mountain():

		print ">>>>>>>>>>>>>>>>>>>>>>>"
		print """Welcome, %s, in these mountains you shall become a mighty magician" % name
		For now, you have to choose what you want to do.
		You can go on training and acquire some additional skills, or go straight to battle.
		Pick \"Battle\" or \"Training\" """
		
		first_quest = raw_input("> ")
		
		
		
		if first_weapon in ('Training', 'training'):
			print ">>>>>>>>>>>>>>>>>>>"
			print "Welcome to training, %s" % name
			
		if first_quest in ('Battle', 'battle'):
			print ">>>>>>>>>>>>>>>>>>>>>"
			print "Welcome to battle, %s" % name
				
		
user_class()
spawn()

