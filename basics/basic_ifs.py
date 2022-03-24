# a very basic if conditional
# however remember that == is case sensitive
cars = ['audi', 'bmw', 'honda', 'subaru']

for car in cars:
  if car == 'bmw':
    print(car.upper())
  else:
    print(car.title())

# check for inequality
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
  print("Hold the anchovies!")

# numerical comparisons
answer = 17
if answer != 42:
  print("That is not the correct answer. Please try again!")

# compare a value to a list 
allergy = 'onions'
toppings = ['mushrooms', 'pepperoni', 'onions', 'cheese', 'marinara']

if allergy not in toppings:
  print("This pizza is safe for allergies.")
else:
  print("This pizza is not safe for allergies!")

# numeric conditionals
age = 19
if age >= 18:
  print("You are old enough to vote!")

# elif numeric conditional
age = 20

if age < 18:
  print("You are not old enough to vote or drink.")
elif age < 21:
  print("You are old enough to vote, but you're not old enough to drink.")
else:
  print("You are old enough to vote and drink!")

# another example
age = 12

if age < 4:
  price = 0
elif age < 18:
  price = 25
else:
  price = 40

print(f"Your admission is ${price}.")

# when an elif clause resolves to True, the rest of the clauses are skipped
# make sure this is desired behavior
# an else instead of last elif would probably be what you want here
name = 'Carol'
age = 3000
if name == 'Alice':
  print('Hi Alice')
elif age < 12:
  print('You are not Alice, kiddo.')
elif age > 100:
  print('You are not Alice, granny.')
elif age > 2000:
  print('Unlike you, Alice is not an undead vampire.')