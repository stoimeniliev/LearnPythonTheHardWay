## Animal is-a object (yes, sort of confusing) look at the extra credit
animals = [dog, cat, fish, person]
person = {dog : }
class Animal(object):
	pass
	
## dog is na animal

class Dog(Animal):
	
	def __init_(self, name):
		## name is dog
		self.name = name
		
## ?? cat is an aninal
class Cat(Animal):

	def __init__(self, name):
		## name is a cat
		self.name = name
		
## person is a object
class Person(object):
	
	def __init__(self, name):
		## name is the persons name
		self.name = name
		
		## Person has-a pet of some kind
		self.pet = None
		
## ??
class Employee(Person):

	def __init__(self, name, salary):
		## ?? hmm what is this strange magic?
		super(Employee, self).__init__(name)
		## ??
		self.salary = salary
		
## ??
class Fish(object):
	pass
	
class Salmon(Fish):
	pass	

	## ??
class Halibut(Fish):
	pass
	
## rover is-a Dog
rover = Dog("Rover")

## ??
satan = Cat("Satan")

## ??
mary = Person("Mary")

## ??
mary.pet = satan

## ??
frank = Employee("Frank", 120000)

## ??
frank.pet = rover

## ??
flipper = Fish()

## ??
crouse = Salmon()

## ??
harry = Halibut()