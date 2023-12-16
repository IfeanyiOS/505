#step1- checking if number is greater than 0
while True:
    user_input= int(input('Enter the number>0:'))
    if user_input <= 0:
        print("Invalid, Enter a number greater than zero")
    else:
        print("Successful, number greater than 0")
        break
# step2- checking if input is an odd or even number
if user_input%2==0:
    print("Number is an even number")
elif user_input%2!=0:
    print("Number is odd")

#step3 - checking if input is a prime nummber or not
for i in range (2,int(user_input**0.5)+1):
    if (user_input % i)==1:
        print("Number is a prime number")
        break
    else:
        print("Number is not a prime number")
        continue

