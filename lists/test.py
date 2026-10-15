# list is build in data type used to store collections of items. They are ordered, changeable and allow duplicates.

l1 = ["RAG", "is", "awesome"]
print(f"Original list: {l1}")

l1.append("!")
print(f"List after adding '!': {l1}")

l1.remove("awesome")
print(f"List after removing 'awesome': {l1}")

result = l1.append("this is a test")
print(result)

# methods which mutate the data type mostly return None


# List comprehensions
# Simpler alternatives to for loops and small performance gain as well why ? these functions run on c compiler while for loop run on python environment

squares = [x**2 for x in range(10)]
print(f"squares of numbers from 0 to 9: {squares}")

squares_for_loop = []
for x in range(10):
    squares_for_loop.append(x**2)
print(f"squares of numbers from 0 to 9: {squares_for_loop}")


# conditional list comprehension
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"squares of even numbers from 0 to 9: {even_squares}")

even_squares_for_loop = []
for x in range(10):
    if x % 2 == 0:
        even_squares_for_loop.append(x**2)
print(f"squares of even numbers from 0 to 9: {even_squares_for_loop}")
