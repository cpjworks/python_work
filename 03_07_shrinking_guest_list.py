# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t
# arrive in time for the dinner, and you have space for only two guests.

guests = ["malcolm", "tosk", "grandfather", "grandmother"]
print(f"Helo {guests[0].title()}. You are warmly invited to a dinner gathering. We have a bigger dining table!")
print(f"Helo {guests[1].title()}. You are warmly invited to a dinner gathering. We have a bigger dining table!")
print(f"Helo {guests[2].title()}. You are warmly invited to a dinner gathering. We have a bigger dining table!")
print(f"Helo {guests[3].title()}. You are warmly invited to a dinner gathering. We have a bigger dining table!")
print(guests)

guests.insert(0, "dad")
print(guests)

guests.insert(3, "mum")
print(guests)

guests.append("sister")
print(guests)

# • Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.

print(f"Helo {guests[0].title()}. I'm afraid I made a mistake and only have space for two for dinner :(")
print(f"Helo {guests[1].title()}. I'm afraid I made a mistake and only have space for two for dinner :(")
print(f"Helo {guests[2].title()}. I'm afraid I made a mistake and only have space for two for dinner :(")
print(f"Helo {guests[3].title()}. I'm afraid I made a mistake and only have space for two for dinner :(")
print(f"Helo {guests[4].title()}. I'm afraid I made a mistake and only have space for two for dinner :(")
print(f"Helo {guests[5].title()}. I'm afraid I made a mistake and only have space for two for dinner :(")
print(f"Helo {guests[6].title()}. I'm afraid I made a mistake and only have space for two for dinner :(")

# • Use pop() to remove guests from your list one at a time until only two
# names remain in your list. Each time you pop a name from your list, print
# a message to that person letting them know you’re sorry you can’t invite
# them to dinner.

popped_guests_6 = guests.pop()
print(f"Dear {popped_guests_6.title()}, I'm so sorry but we will have to re-arrange, as I do not have space to accommodate everyone this evening.")

popped_guests_5 = guests.pop()
print(f"Dear {popped_guests_6.title()}, I'm so sorry but we will have to re-arrange, as I do not have space to accommodate everyone this evening.")

popped_guests_4 = guests.pop()
print(f"Dear {popped_guests_6.title()}, I'm so sorry but we will have to re-arrange, as I do not have space to accommodate everyone this evening.")

popped_guests_3 = guests.pop()
print(f"Dear {popped_guests_6.title()}, I'm so sorry but we will have to re-arrange, as I do not have space to accommodate everyone this evening.")

popped_guests_2 = guests.pop()
print(f"Dear {popped_guests_6.title()}, I'm so sorry but we will have to re-arrange, as I do not have space to accommodate everyone this evening.")
print(guests)

# • Print a message to each of the two people still on your list, letting them
# know they’re still invited.

print(f"Helo {guests[0].title()} and {guests[1].title()}. I'm pleased to say that both of you are still welcome for dinner this evening.")

# • Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end
# of your program.

del guests[0]
del guests[0]
print(guests)