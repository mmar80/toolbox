# a tuple is an immutable list.
# tuples look just like lists except they have () instead of []
dimensions = (200,50)
# try to change one of the tuple elements
#dimensions[0] = 250

# loop over a tuple
for dimension in dimensions:
  print(dimension)

# you can't change a tuple, but you can reassign the var itself
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
  print(dimension)