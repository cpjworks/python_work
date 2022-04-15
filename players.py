# Learning how to use "slice" to access cetain elements within a list: [item 1:item 2]

players = ["charles", "martina", "michael", "florence", "eli"]
print(players[0:3])
print(players[1:4])
print(players[:5])
print(players[2:])

print("Here are the first three players in my team:")
for player in players[0:3]:
    print(player.title())
