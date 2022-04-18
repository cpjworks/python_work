# 4-15. Code Review: Choose three of the programs you’ve written in this 
# chapter and modify each one to comply with PEP 8:
# • Use four spaces for each indentation level. Set your text editor to insert
# four spaces every time you press tab, if you haven’t already done so (see
# Appendix B for instructions on how to do this).
# • Use less than 80 characters on each line, and set your editor to show a
# vertical guideline at the 80th character position.
# • Don’t use blank lines excessively in your program files.


# Program 01:
# 4-13. Buffet: A buffet-style restaurant offers only five basic foods.
# Think of five simple foods, and store them in a tuple.

foods = ("bread", "rice", "beans", "soup", "corn")
print("Old menu:")

# • Use a for loop to print each food the restaurant offers.

for food in foods:
    print(food)

# • Try to modify one of the items, and make sure that Python rejects the 
# change.

# • The restaurant changes its menu, replacing two of the items with different
# foods. Add a line that rewrites the tuple, and then use a for loop to print
# each of the items on the revised menu.

foods = foods = ("bread", "rice", "potatoes", "soup", "mushy peas")
print("\nNew menu:")
for food in foods:
    print(food)


# Program 02:
# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
# (page 56). Make a copy of the list of pizzas, and call it friend_pizzas.

my_pizzas = ["seafood", "vegetarian", "hawaiian", "florentine"]
friends_pizzas = my_pizzas[:]
print(friends_pizzas)

# Then, do the following:
# • Add a new pizza to the original list.

my_pizzas.append("mushroom")

# • Add a different pizza to the list friend_pizzas.

friends_pizzas.append("meat feast")

# • Prove that you have two separate lists. Print the message My favorite
# pizzas are:, and then use a for loop to print the first list. 

print("My favourite pizzas are:")
for my_pizza in my_pizzas:
    print(my_pizza.title())

# Print the message My friend’s favorite pizzas are:, 
# and then use a for loop to print the second list. 
# Make sure each new pizza is stored in the appropriate list.

print("\nMy friend's favourite pizzas are:")
for friends_pizza in friends_pizzas:
    print(friends_pizza.title())


# Program 03:
# 4-2. Animals: Think of at least three different animals that have a 
# common characteristic. Store the names of these animals in a list, and 
# then use a for loop to print out the name of each animal.

animals = ["cats", "dogs", "bears", "otters", "pigs"]
for animal in animals:
    print(animal.title())

# • Modify your program to print a statement about each animal, such as
# A dog would make a great pet.

animals = ["cats", "dogs", "bears", "otters", "pigs"]
for animal in animals:
    print(f"{animal.title()} are so friendly and cute. \
I would like one as a flatmate someday.")

# • Add a line at the end of your program stating what these animals have in
# common. You could print a sentence such as Any of these animals would 
# make a great pet!

animals = ["cats", "dogs", "bears", "otters", "pigs"]
for animal in animals:
    print(
    f"{animal.title()} are so friendly and cute. \
I would like one as a flatmate someday.\n")

print("All of these magnificent beasts have four legs, \
two eyes, one nose, and buckets of character.")