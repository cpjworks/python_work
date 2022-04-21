# 5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an 
# if-elif-else chain.
# • If the alien is green, print a message that the player earned 5 points.
# • If the alien is yellow, print a message that the player earned 10 points.
# • If the alien is red, print a message that the player earned 15 points.
# • Write three versions of this program, making sure each message is printed
# for the appropriate color alien.

alien = "green" 
if alien == "green":
    print("You just got yourself 5 points!")
elif alien == "yellow":
    print("Wow! 10 points! Keep going!")
else:
    print("Red! 15 points, yeah!")


alien = "yellow" 
if alien == "green":
    print("You just got yourself 5 points!")
elif alien == "yellow":
    print("Wow! 10 points! Keep going!")
else:
    print("Red! 15 points, yeah!")


alien = "red" 
if alien == "green":
    print("You just got yourself 5 points!")
elif alien == "yellow":
    print("Wow! 10 points! Keep going!")
else:
    print("Red! 15 points, yeah!")