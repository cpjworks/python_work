# Learning how to make copies of lists with "slice"

my_foods = ["pizza", "falafel", "carrot cake"]
friends_foods = my_foods[:]

my_foods.append("seafood")
friends_foods.append("beef noodle")

print("My favourite foods are:")
print(my_foods)

print("\nMy friend's favourite foods are:")
print(friends_foods)

