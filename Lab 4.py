# Step1- create a new python file (Lab4)
# Step2- using for loop statement to print the numbers from 0-10
for i in range(11):
    print(i, end="")
# Step3- using for loop statement to print numbers from 1-10
for i in range(1,10):
    print(i)
# Step4- using for loop statement to print numbers from 1-10 with increment of 2
for i in range(1,10,2):
   print(i,end="")
# Step5- calculate the area of a circle
Radius= int(input("\n Enter the radius of a circle:"))
# Step6- using math function to generate the value for Pi
import math
pi = input(math.pi)
# Step7- calculating the area of a circle
Area = math.pi*Radius**2
print("Area=", Area)
# Step8- using the input function to  collect the value for the length of a rectangle
Length= int(input("Enter the length of a rectangle:"))
# Step9- using the input function to collect the value for the width of a rectangle
Width= int(input("Enter the width of a rectangle:"))
# Step10- calculating the Area of a rectangle
Area_R= Length*Width
# Step11- modifying steps 7 and 10 using if-else statement
if Area>0:
    print("Area=", Area)
else:
    print("Area=","Can't compute the area of a circle")
if Area_R>0:
    print("Area_R=", Area_R)
else:
    print("Area_R=","Can't compute the area of a rectangle")
