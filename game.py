from random import randint

hero = {'lvl' : 1,
		'exp' : 0,
		'nextlvl' : 50}
		'stats' : {'dmg' : [5, 12]),
					'hp' : 100,
					}
		 }
		 
enemy = {'lvl' : 1,
		'exp' : 0,
		'nextlvl' : 50}
		'dmg' : [2, 6]),
		'hp' : 30,
					
		 }

		 
def lvlup(hero):
	while hero['exp'] >= hero['nextlvl']:
		hero['lvl'] += 1
		hero['exp'] += hero['exp'] - hero['nextlevel']
		hero['nextlvl'] = round(hero['nextlvl'] * 1.5)
		hero['hp'] = hero['hp'] + round(hero['hp'] * 0.2)
		hero['dmg'] = hero['dmg'] + round(hero['dmg'] * 0.3)
		
		print "The level of the hero is %d, his damage is %d, his hp is %d, exp to next level is %d" % (hero['lvl'], hero['dmg'], hero['hp'], hero['nextlvl'])
		
def damaged(player, monster)
	atk = randint(player['dmg'][0], player['dmg'][1])
	monster['hp'] = monster['hp'] - atk
		if monster['hp'] <= 0:
			print('{} has been slain'.format(monster['name']))
		else:
			print('{} takes {} damage!'.format(monster['name'], atk))
			
def commands(char, foe):
	while True:
		print('-------------------')
		cmd = input('Do you want to attack? yes/no: ').lower()
		if 'yes' in cmd:
			damaged(char, foe)
		elif 'no' in cmd:
			print(' {} takes the opportunity to attaack