# 5-9. No Users: Add an if test to hello_admin.py to make sure the list 
# of users is not empty.

usernames = ["admin", "josh", "anna", "ari", "katie", "smith"]

if usernames:
    for username in usernames:
        if username == "admin":
            print("Hello admin. Would you like to see a status report?")
        else:
            print(f"Hello {username.title()}. How are you today?")
else:
    print("We need more users!")


# • If the list is empty, print the message We need to find some users!
# • Remove all of the usernames from your list, and make sure the correct
# message is printed.

usernames = []

if usernames:
    for username in usernames:
        if username == "admin":
            print("Hello admin. Would you like to see a status report?")
        else:
            print(f"Hello {username.title()}. How are you today?")
else:
    print("We need more users!")
    