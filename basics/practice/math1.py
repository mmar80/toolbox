# use a for loop to print all numbers 1-20
for value in range(1, 21):
  print(value)

# make a list of numbers 1-1,000,000 then use for loop to print numbers
# commented out because it takes a while to run
#numbers = list(range(1, 1000001))
#for number in numbers:
#  print(number)

# make a list of numbers 1-1,000,000 and then use min(), max() and sum()
numbers = list(range(1, 1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# make a list of odd numbers 1-20, use a for loop to print each
odd_numbers = list(range(1, 21, 2))
for odd_number in odd_numbers:
  print(odd_number)

# make a list of multiple of 3 from 3 to 30, use a for loop to print each
multiples_of_3 = list(range(0, 31, 3))
for multiple_of_3 in multiples_of_3:
  print(multiple_of_3)

# make a list of the first 10 cubes (that is, the cube of each integer 1-10)
# use a for loop to print out the values
cubes = [value**3 for value in range(1,11)]
print(cubes)