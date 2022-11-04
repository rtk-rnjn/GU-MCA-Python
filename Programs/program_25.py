# Python program for random module

import random

# Printing random integer between 0 and 5
print("The random integer is : ", end="")
print(random.randint(0, 5))

# Printing random float between 0 and 1
print("The random float is : ", end="")
print(random.random())

# Printing random element from list
print("The random element from list is : ", end="")
print(random.choice([1, 3, 5, 7, 9]))

# Printing random element from string
print("The random character from string is : ", end="")
print(random.choice("Python"))

# Printing random element from range
print("The random character from range is : ", end="")
print(random.choice(range(10)))

# Printing random element from tuple
print("The random character from tuple is : ", end="")
print(random.choice((1, 3, 5, 7, 9)))

# Printing random element from set
print("The random character from set is : ", end="")
print(random.choice({1, 3, 5, 7, 9}))

# Printing random element from frozen set
print("The random character from frozen set is : ", end="")
print(random.choice(frozenset({1, 3, 5, 7, 9})))

# Printing random element from dictionary
print("The random character from dictionary is : ", end="")
print(random.choice({1: "one", 2: "two", 3: "three"}))

# Printing random element from bytes
print("The random character from bytes is : ", end="")
print(random.choice(b"Python"))

# Printing random element from bytearray
print("The random character from bytearray is : ", end="")
print(random.choice(bytearray(b"Python")))
