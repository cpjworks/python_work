# 3-10. Every Function: Think of something you could store in a list. For example,
# you could make a list of mountains, rivers, countries, cities, languages, or anything
# else you’d like. 

# Write a program that creates a list containing these items
# and then uses each function introduced in this chapter at least once:

# Functions to use:

# 1. Print indexed items from list
games = ["metal gear solid", "final fantasy 12", "advance wars", "nier", "talos principle"]
print(games)

# 2. Print indexed from end of list
print(games[4].title())
print(games[-2].title())

# 3. Change value of indexed item
games[1] = "final fantasy 7"
print(games)

# 4. Use append to add items to end of list
games.append("halo")
print(games)

# 5. Use append to build a new list from scratch
games = []
games.append("shenmue")
games.append("super monkey ball")
games.append("soul calibur")
games.append("skies of arcadia")
games.append("the wind waker")
print(games)

# 6. Use insert to add a new item to a specific index location
games.insert(2, "street fighter iii: 3rd strike")
print(games)

# 7. Use del statement to remove item(s) from list at index location
del games[4]
print(games)

# 8. Remove last item from list using pop, save value, and re-use
popped_game = games.pop()
print(games)
print(popped_game)
games.append(popped_game)
print(games)

# 9. Pop specific item using index location
games.pop(1)
print(games)
games.append("super monkey ball")
print(games)

# 10. Remove item(s) by value (name)
games.remove ("soul calibur")
print(games)

# 11. Use sort to change order permanently
games.sort()
print(games)

# 12. Reverse sort
games.sort(reverse = True)
print(games)

# 13. Sorted to rearrange but not permanent
games = ["metal gear solid", "final fantasy 12", "advance wars", "nier", "talos principle"]
print(sorted(games))

# 13. Reverse sorted
print(sorted(games, reverse=True))

# 14. Reverse method
games.reverse()
print(games)

# 14. Use len to find length of list
games = ["metal gear solid", "final fantasy 12", "advance wars", "nier", "talos principle"]
print(len(games))
