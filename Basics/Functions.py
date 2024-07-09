def calculateGmean(a, b): #Function declared
    mean = (a*b)/(a+b)
    print(mean)

num1 = 34
num2 = 45
calculateGmean(num1, num2) #Function called


#Function to calculate greater number between two variables.
def Isgreater(a, b):
    if (a > b):
        print(str(a) + " is greater than " + str(b))
    elif (b > a):
        print(str(b) + " is greater than " + str(a))
    else:
        print(str(a) + " and " + str(b) + " are equal")

num1 = int(input("Enter your first num: "))
num2 = int(input("Enter your second num: "))
Isgreater(num1, num2)