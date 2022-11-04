# Python program for statistics module

import statistics

# Declaring list of elements
a = [1, 3, 4, 2, 6, 5, 3, 4, 5, 2]

# Calculating mean
print("The mean is : ", end="")
print(statistics.mean(a))

# Calculating median
print("The median is : ", end="")
print(statistics.median(a))

# Calculating mode
print("The mode is : ", end="")
print(statistics.mode(a))

# Calculating standard deviation
print("The standard deviation is : ", end="")
print(statistics.stdev(a))

# Calculating variance
print("The variance is : ", end="")
print(statistics.variance(a))
