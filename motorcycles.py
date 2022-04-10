# Practicing how to replace indexed items in a list.

motorcycles = ["yamaha", "suzuki", "honda"]
motorcycles[0] = "ducati"
print(motorcycles)
motorcycles.append("yamaha")
print(motorcycles)


motorcycles2 = []
motorcycles2.append("triumph")
motorcycles2.append("norton")
motorcycles2.append("kawasaki")
print(motorcycles2)

motorcycles2.insert(0, "harley")
print(motorcycles2)

del motorcycles2[3]
print(motorcycles2)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}")

motorcycles2.remove("norton")
print(motorcycles2)

motorcycles3 = ["ducati", "yamaha", "suzuki", "honda"]
print(motorcycles3)
too_expensive = "ducati"
motorcycles3.remove(too_expensive)
print(motorcycles3)
print(f"\nA {too_expensive.title()} is too expensive for me.")
