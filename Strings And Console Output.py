#Strings
# Set the variable brian on line 3
brian = "Hello life"
"Hello brian"

# Assign your variables below, each on its own line!

caesar = "Graham"
praline = "John"
viking = "Teresa"
# Put your variables above this line

print(caesar)
print(praline)
print(viking)

# Escaping characters
'This isn\'t flying, this is falling with style!'

# Access by index
"""
The string "PYTHON" has six characters,
numbered 0 to 5, as shown below:

+---+---+---+---+---+---+
| P | Y | T | H | O | N |
+---+---+---+---+---+---+
  0   1   2   3   4   5

So if you wanted "Y", you could just type
"PYTHON"[1] (always start counting from 0!)
"""
fifth_letter = "MONTY"[4]

print(fifth_letter)

# String methods
parrot = "Norwegian BLue"
print((len(parrot)))

# lower
parrot = "Norwegian Blue"
"Norwegian BLue".lower
print(parrot.lower())

# upper
parrot = "norwegian blue"
"norwgegian blue".upper()
print(parrot.upper())

# str method
"""Declare and assign your variable on line 4,
then call your method on line 5!"""

pi = 3.14
print(str(pi))

# Dot Notation
ministry = "The Ministry of Silly Walks"

print(len(ministry))
print(ministry.upper())

# Print strings
print("Monty Python")

# Printing variables
the_machine_goes = "Ping!"
print(the_machine_goes)

# String Concatenation
print("Spam " + "and " + "eggs")

# Explicit String Conversion
print("The value of pi is around " + str ("3.14"))

# String Formatting with %, Part 1
string_1 = "Camelot"
string_2 = "place"

print("Let's not go to %s. 'Tis a silly %s." % (string_1, string_2))

# String Formatting with %, Part 2
name = "Alex"
quest = "Teaching Python"
color = "Blue"

print("Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color))

# Creation, Methods, Print
my_string = "Bravo"
print(len(my_string))
print(my_string.upper())