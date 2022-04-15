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

# Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second
# list. Make sure each new pizza is stored in the appropriate list.

print("\nMy friend's favourite pizzas are:")
for friends_pizza in friends_pizzas:
     print(friends_pizza.title())
