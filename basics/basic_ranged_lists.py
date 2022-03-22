# range() makes it easy to generate a series of numbers
# remember index begins at 0 and a range does not include the last number
for value in range(1, 5):
  print(value)

# to generate a list from a range()
numbers = list(range(1, 6))
print(numbers)

# range() can take an optional 3rd parameter, the 'step' (interval)
# see docs here https://docs.python.org/3/library/stdtypes.html#ranges
# use step to grab only the even numbers in a list
even_numbers = list(range(2,11,2))
print(even_numbers)

# make a list of the first 10 square numbers
# ** = exponents in python
squares = []
for value in range(1,11):
  square = value ** 2
  squares.append(square)
print(squares)

# a more concise version of the above
squares = []
for value in range(1,11):
  squares.append(value**2)
print(squares)

# a version of the above using list comprehension
squares = [value**2 for value in range(1,11)]
print(squares)

# basic stats functions examples
# if you don't pass a start value in the range(0) it will default to 0
numbers = list(range(10))
print(min(numbers))
print(max(numbers))
print(sum(numbers))
