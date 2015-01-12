i = 0
numbers = []

f = int(raw_input("> "))
g = int(raw_input("> "))

def ciment(i):
	for i in range(f, g):
		print "at the top i is %d" % i
		numbers.append(i)
	
		i=i+g
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	
print ciment(i)
print "The numbers: "

for num in numbers:
	print num