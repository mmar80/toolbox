# store five foods in a tuple
foods = ('lo mein', 'broccoli and chicken', 'oyster beef', 'fried rice', 'sesame chicken')

# use a for loop to print each item at the buffet
print("\nWelcome to the buffet! Today's items are:\n")
for food in foods:
  print(food.title())

# try to modify the tuple (and fail)
#foods.append('humbow')

# the restaurant changed its menu.. update the available foods
foods = ('lo mein', 'fried rice', 'orange chicken', 'kung pao chicken', 'sichuan fish')
print("\nThe buffet has updated its menu. Today's availabilities are:\n")
for food in foods:
  print(food.title())