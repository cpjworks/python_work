# 5-8. Hello Admin: Make a list of five or more usernames, including the 
# name'admin'. 

usernames = ["admin", "josh", "anna", "ari", "katie", "smith"]

# Imagine you are writing code that will print a greeting to 
# each user after they log in to a website. Loop through the list, and print 
# a greeting to each user:

for username in usernames:
    if username == "admin":
        print("Hello admin. Would you like to see a status report?")
    else:
        print(f"Hello {username.title()}. How are you today?")


# • If the username is 'admin', print a special greeting, such as Hello admin,
# would you like to see a status report?

# • Otherwise, print a generic greeting, such as Hello Jaden, thank you for
# logging in again.
