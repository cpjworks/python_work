# Using range and integers to calculate square numbers / exponents.

squares = []
for value in range(1, 11):
    squares.append(value**2)

print(squares)


# Same output but using List Comprehensions, which combinine the for loop,
# creation of new elements, and appending those elements.
squares = [value**2 for value in range (1, 11)]
print(squares)
