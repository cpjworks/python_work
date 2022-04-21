# 5-2. More Conditional Tests: You don’t have to limit the number of tests you
# create to ten. If you want to try more comparisons, write more tests and add
# them to conditional_tests.py. Have at least one True and one False result for
# each of the following:
# • Tests for equality and inequality with strings

game = "puyo puyo"
print("Is game == 'puyo puyo'? I predict True.")
print(game == "puyo puyo")
print("Is game == 'puyo puyo'? I predict False.")
print(game == "shenmue")

# • Tests using the lower() method

pencil = "Hi Uni"
print("\nIs pencil == 'Hi Uni'? I predict True.")
print(pencil.lower() == "hi uni")
print("Is pencil == 'Mars'? I predict False.")
print(pencil.lower() == "mars")

# • Numerical tests involving equality and inequality, greater than and
# less than, greater than or equal to, and less than or equal to

cups_of_hot_chocolate = 5
print("\nIs cups_of_hot_chocolate == 5? I predict True.")
print(cups_of_hot_chocolate == 5)
print("Is cups_of_hot_chocolate == 1? I predict False.")
print(cups_of_hot_chocolate == 1)

laptop_price = 2119
print("\nIs laptop_price > 2000? I predict True.")
print(laptop_price > 2000)
print("Is laptop_price > 2500? I predict False.")
print(laptop_price > 2500)

print("\nIs laptop_price < 2200? I predict True.")
print(laptop_price < 2200)
print("Is laptop_price < 2000? I predict False.")
print(laptop_price < 2000)

turtles_in_pond = 30
print("\nIs turtles_in_pond >= 20? I predict True.")
print(turtles_in_pond >= 20)
print("Is turtles_in_pond >= 50? I predict False.")
print(turtles_in_pond >= 50)

meals_per_day = 3
print("\nIs meals_per_day <= 3? I predict True.")
print(meals_per_day <= 3)
print("Is meals_per_day <= 2? I predict False.")
print(meals_per_day <= 2)

# • Tests using the and keyword and the or keyword

orange_fish = 20
red_fish = 5
print("\nAre there 20 orange_fish and more than 3 red_fish? I predict True.")
print(orange_fish == 20 and red_fish > 3)
print("Are there 10 orange_fish and more than 3 red_fish? I predict False.")
print(orange_fish == 10 and red_fish > 3)

print("\nAre there 20 orange_fish or 5 red_fish? I predict True.")
print(orange_fish == 20 or red_fish == 1)
print("Are there 20 orange_fish or 5 red_fish? I predict True.")
print(orange_fish == 15 or red_fish == 3)

# • Test whether an item is in a list

music = ["rock", "grunge", "hip-hop", "classical", "country"]
print("\nIs classical music in the list? I predict True.")
print("classical" in music)

# • Test whether an item is not in a list

print("Is psytrance music in the list? I predict False.")
print("psytrance" in music)
