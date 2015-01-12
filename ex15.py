from sys import argv #importing the libraries

script, filename = argv # unpacking the variables

txt = open(filename) #variable txt is the file that we open

print "Here's your file %r:" % filename #
print txt.read() #we are reading the opened file

print "Type the filename again:"
file_again = raw_input("> ") # another way to enter the file

txt_again = open(file_again) # another way to open the file

print txt_again.read() #