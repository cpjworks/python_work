# 4-2. Animals: Think of at least three different animals that have a common characteristic.
# Store the names of these animals in a list, and then use a for loop to
# print out the name of each animal.

animals = ["cats", "dogs", "bears", "otters", "pigs"]
for animal in animals:
    print(animal.title())

# • Modify your program to print a statement about each animal, such as
# A dog would make a great pet.

animals = ["cats", "dogs", "bears", "otters", "pigs"]
for animal in animals:
    print(f"{animal.title()} are so friendly and cute. I would like one as a flatmate someday.")

# • Add a line at the end of your program stating what these animals have in
# common. You could print a sentence such as Any of these animals would make a great pet!

animals = ["cats", "dogs", "bears", "otters", "pigs"]
for animal in animals:
    print(f"{animal.title()} are so friendly and cute. I would like one as a flatmate someday.\n")
print("All of these magnificent beasts have four legs, two eyes, one nose, and buckets of character.")