name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
heightcm = height * 2.54
weightkg = weight * 0.45

print "Let's talk about %s." % name
print "He's %r inches tall. That's %r centimeters." % (height, heightcm)
print "He's %d pounds heavy. That's %d kilograms" % (weight, weightkg)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d" % (age, height, weight, age + height + weight)