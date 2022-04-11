# 3-6. More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.

# • Start with your program from Exercise 3-4 or Exercise 3-5. Add a print()
# call to the end of your program informing people that you found a bigger
# dinner table.

# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.

# • Print a new set of invitation messages, one for each person in your list.

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

print(f"Helo {guests[0].title()}. You are warmly invited to a dinner gathering. There are going to be lots of us!")
print(f"Helo {guests[1].title()}. You are warmly invited to a dinner gathering. There are going to be lots of us!")
print(f"Helo {guests[2].title()}. You are warmly invited to a dinner gathering. There are going to be lots of us!")
print(f"Helo {guests[3].title()}. You are warmly invited to a dinner gathering. There are going to be lots of us!")
print(f"Helo {guests[4].title()}. You are warmly invited to a dinner gathering. There are going to be lots of us!")
print(f"Helo {guests[5].title()}. You are warmly invited to a dinner gathering. There are going to be lots of us!")
print(f"Helo {guests[6].title()}. You are warmly invited to a dinner gathering. There are going to be lots of us!")