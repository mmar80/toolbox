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
print(f"\nA {too_expensive.title()} is too expensive for me.")