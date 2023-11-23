# Step1-create a python lab_5 file
# Step2- collecting input for user
number1=int(input("Enter number 1:"))
# Step3- using if statement to check if input is  divisible by 3 and 5
for number1 in range(1,number1):
    if (number1 %3==0) and (number1 %5==0):
        print(number1, "Tic Tac")
# Step4- using the if statement to check if input is divisible by 3
    if(number1%3==0):
        print(number1,"Tic")
# Step5- using the if statement to check if input is divisible by 5
    if(number1%5==0):
        print(number1,"Tac")
# Step6- using while loop statement to print numbers from 1-20
a=1
while a<21:
    a+=1
    print(a)
# Step7- using while loop statement to modify code in step 6
input1=int(input("Enter input1:"))
input1=1
while input1<16:
    input1+=1
    if input1%3==0 and input1%5==0:
        print(input1,"Tic Tac")
    elif input1%3==0:
        print(input1,"Tic")
    elif input1%5==0:
        print(input1,"Tac")
# Step8- using random_generator function to generate random numbers
import random
print(random.randint(20,50))
""" Step9- using while loop and if-else statement to collect a value from a user
and also check if the value is greater than 0 (>0) or not 
"""
limit=5
while limit>0:
    user_value = int(input("Enter the value:"))
    if user_value>0:
        print(user_value,"\n Successful")
        break
    else:
        limit-=1
        print("invalid entry \n please enter a valid value")
""" Step 10- using the random_generator function to generate int value 
if the input from step 9 is greater than 0
"""
import random
user_value = int(input("Enter int value:"))
random_value= random.randint(1,user_value)
limit = 0
while True:
    limit+= 1
    my_value = int(input("first value:"))
# if my_value==random_value, display output ("Perfect") and end loop
    if my_value== random_value:
        print("Perfect")
        break
# else, display output("both numbers don't match") and continue loop
    else:
        print("both numbers don't match")








