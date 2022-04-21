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

print("Finished making your pizza!")


# Using if statements with lists:

requested_toppings = ["mushrooms", "green peppers", "extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print("Sorry, we are out of green peppers.")
    else:
        print(f"Adding {requested_topping}.")

print("Finished making your pizza!")

