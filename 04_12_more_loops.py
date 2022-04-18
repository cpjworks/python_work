# 4-12. More Loops: All versions of foods.py in this section have avoided using
# for loops when printing to save space. 

my_foods = ["pizza", "falafel", "carrot cake"]
friends_foods = my_foods[:]

my_foods.append("seafood")
friends_foods.append("beef noodle")

print("My favourite foods are:")
print(my_foods)

print("\nMy friend's favourite foods are:")
print(friends_foods)

# Choose a version of foods.py, and write two for loops to print each list of foods.

for my_food in my_foods:
    print(my_food)

for friends_food in friends_foods:
    print(friends_food)
    