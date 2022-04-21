# Checking for inequalities in "if" statements.
# Using mutiple if statements if several tests might be True.
# Do not use if-elif-else chain in this case.

requested_toppings = ["mushrooms", "extra cheese"]

if "mushrooms" in requested_toppings:
    print("Adding mushrooms.")
if "pepperoni" in requested_toppings:
    print("Adding pepperoni.")
if "extra cheese" in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")
