# Python program for collection module

import collections

# Declaring namedtuple()
Student = collections.namedtuple("Student", ["name", "age", "DOB"])

# Adding values
S = Student("Nandini", "19", "2541997")

# Access using index
print("The Student age using index is : ", end="")
print(S[1])

# Access using name
print("The Student name using keyname is : ", end="")
print(S.name)

# Access using getattr()
print("The Student DOB using getattr() is : ", end="")
print(getattr(S, "DOB"))

# Declaring Counter()
a = [1, 4, 5, 6, 9, 9, 9]
b = [1, 2, 3, 5, 7, 9, 9, 9]

# using counter elements
print("The elements with their counts are : ", end="")
print(collections.Counter(a))

# using counter elements from
# an iterable
print("The counts of elements in list are : ", end="")
print(collections.Counter(b))

# Declaring deque()
DoubleEnded = collections.deque(["Mon", "Tue", "Wed"])

# Adding to the right
print("The deque after adding to the right is : ", end="")
print(DoubleEnded)

# Adding to the left
DoubleEnded.appendleft("Sun")
print("The deque after adding to the left is : ", end="")
print(DoubleEnded)

# Removing from the right
print("The deque after removing from the right is : ", end="")
print(DoubleEnded)

# Removing from the left
print("The deque after removing from the left is : ", end="")
print(DoubleEnded)
