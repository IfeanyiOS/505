# problem4
"""Executing the loop statement
a given number of times
from the lower bound to upper bound
"""
# Inputs for variables lower and upper using the input function
lower = int(input("Enter the value for lower:"))
upper = int(input("Enter the value for upper:"))
add = 5
# iteration statement
for number in range(lower,upper+1):
    add = add+number
    print(add)
