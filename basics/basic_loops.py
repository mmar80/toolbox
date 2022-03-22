# simple loop
magicians = ['alice', 'bob', 'caroline']
for magician in magicians:
  print(magician)

# each indented line is considered 'in the loop' and will be executed
# once for each value in the list
magicians = ['andy', 'beth', 'chris']
for magician in magicians:
  print(f"{magician.title()}, nice trick!")
  print(f"I am excited to see what you'll do next, {magician.title()}.\n")
# any lines after the for loop will only be executed once
print(f"I hope you enjoyed the magic show!\n\n")

# more loop examples
pizzas = ['mushroom', 'pesto', 'margherita']
for pizza in pizzas:
  print(f"I like a good {pizza} pizza.")
print(f"The pizza here is really great!\n\n")