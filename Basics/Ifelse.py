#Greeting hello ifelse practice

position = input("Enter your job role: ").lower()
print("Your job role is " + position)

if(position == "director"):
    print("Hello director")

elif(position == "manager"):
    print("Hello manager")

elif(position == "employee"):
    print("Hello employee")

elif(position == "intern"):
    print("Hello intern")

else:
    new = input("Are you a new commer?").lower()
    if(new == "yes"):
        print("Hello new commer")
    else:
        print("Thanks for visiting")

#Program to find out if the number is greater or less than 100

num = int(input("Enter your desired number: "))
if (num > 100):
    print("The number " + str(num) + " is greater than 100")
elif (num == 100):
    print("The number " + str(num) + " is equals to 100")
elif (num < 100):
    print("The number " + str(num) + " is less than 100")
else:
    print("Invalid input! please enter again")

#Program to greet user based on the current time

import time
name = input("Enter your name here: ")
current_time = int(time.strftime("%H"))
if 0 <= current_time < 12: 
    print("Good morning " + name )
elif 12 <= current_time < 18:
    print("Good afternoon " + name)
elif 18 <= current_time < 24:
    print("Good evening " + name)
else:
    print("Something went wrong !!")