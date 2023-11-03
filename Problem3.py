# Problem 3:
# Collecting input from five users
user1=int(input("Enter number 1:"))
user2=int(input("Enter number 2:"))
user3=int(input("Enter number 3:"))
user4=int(input("Enter number 4:"))
user5=int(input("Enter number 5:"))
"""inputs- number1:5
number2:10
number3:15
number4:20
number5:25
"""
# addition of the five inputs
add=user1+user2+user3+user4+user5
print("The sum is:", add)
# Final output; sum=75
# calculating the average using the statistics.mean()function
""" To calculate the average, 
we need to import the statistics library
using import statistics function
note: the formula to calculate the average 
average = sum/total number of users(5)
"""
import statistics
print("Average:", statistics.mean([user1, user2, user3, user4, user5]))
# Final output; Average=15
# note that the list[]function was used to list each variable in the sequence

