cars = 100 # broi koli	
space_in_car = 4.0 #svobodni mesta v kola
drivers = 30 #broi shofiori
passengers = 90 #broi pasajeri v kola
cars_not_driven = cars - drivers # koli koito ne se karat e ravno na broikata na kolite 100 - shfiori 30 = 70
cars_driven = drivers #kolite koito se karat sa ravni na shofiorite = 30
carpool_capacity = cars_driven * space_in_car #kolko 4oveka se karat 30*4 = 120
average_passengers_per_car = passengers / cars_driven #sredna broika na pasajeri 90 / 30 = 4


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."