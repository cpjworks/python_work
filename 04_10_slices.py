# 4-10. Slices: Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:

# • Print the message The first three items in the list are:. Then use a slice to
# print the first three items from that program’s list.

print("The first three items in the list are:")
animals = ["cats", "dogs", "bears", "otters", "pigs"]
print(animals[0:3])

# • Print the message Three items from the middle of the list are:. Use a slice to
# print three items from the middle of the list.

print("The middle three items in the list are:")
animals = ["cats", "dogs", "bears", "otters", "pigs"]
print(animals[1:4])

# • Print the message The last three items in the list are:. Use a slice to print the
# last three items in the list.

print("The last three items in the list are:")
animals = ["cats", "dogs", "bears", "otters", "pigs"]
print(animals[-3:])
