# Checking whether a value is not in a list, using "not":

banned_users = ["andrew", "carolina", "david"]
user = "maria"

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
