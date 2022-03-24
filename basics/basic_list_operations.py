# lists are in square brackets, values are comma-separated and enclosed in single quotes
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

# overwrite the item at index 0
motorcycles[0] = 'ducati'
print(motorcycles)

# append into an empty list
motorcycles = []
motorcycles.append('honda')
motorcycles.append('triumph')
motorcycles.append('kawasaki')
print(motorcycles)

# insert into a list (requires index)
motorcycles.insert(0, 'harley')
print(motorcycles)

# remove an item from a list with del statement (requires index)
del motorcycles[0]
print(motorcycles)

# pop() one off for later use
# pop() removes the last item in the list if you don't pass an index
motorcycles = ['honda','ducati','trumph']
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

# pop() can be useful when handling the first or last of a list
motorcycles = ['harley','honda','triumph']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# remove() an item by value
motorcycles = ['honda','tomo','ducati','suzuki']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

# remove() an item and work with it
motorcycles = ['honda','ducati','suzuki','yamaha']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.\n\n")

# slice() examples. slice() doesn't impact the underlying list, the slice() is a copy
# as with range() the index stops before the second value
players = ['anna','blake','caroline','david','emma']
print(players[0:3])
print(players[2:5])
# if you omit the starting index, it will start at the beginning of list
print(players[:5])
# if you omit the second (stopping) index it will go to the end
print(players[2:])
# if you want only the last two items in the list
print(players[-2:])
# as with range(), interval can be passed as optional third param
print(players[1:6:2])

# looping through a slice
players = ['andy', 'beth', 'chris', 'darcy', 'edward', 'francesca']
print("Here are the first three players on my team:")
for player in players[:3]:
  print(player.title())

# copy an entire list into a slice with ([:])
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# append different objects into each list and prove they are different
my_foods.append('ice cream')
print(my_foods)

friend_foods.append('fried mushrooms')
print(friend_foods)

# use a for loop to print the output
bowls = ['poke','katsudon','bulgolgi','roasted veggies']
print("Welcome to World Bowls. Today's bowls are:")
for bowl in bowls:
  print(bowl)