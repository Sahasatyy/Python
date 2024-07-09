Fnum = float(input("Enter your first number: "))
Snum = float(input("Enter your second number: "))
print("1 for addition", "2 for subtracion", "3 for multiplication", "4 for division")
Operation = int(input("Enter your desired operations: "))

if Operation == 1:
    result = Fnum + Snum
    print("The sum of " + str(Fnum) + " and " + str(Snum) + " is " + str(result) + ".")
elif Operation == 2:
    result = Fnum - Snum
    print("The difference of " + str(Fnum) + " and " + str(Snum) + " is " + str(result) + ".")
elif Operation == 3:
    result = Fnum * Snum
    print("The multiplication of " + str(Fnum) + " and " + str(Snum) + " is " + str(result) + ".")
elif Operation == 4:
    result = Fnum / Snum
    print("The division of " + str(Fnum) + " and " + str(Snum) + " is " + str(result) + ".")
else:
    print("Please enter valid operation")
    print("1 for addition", "2 for subtracion", "3 for multiplication", "4 for division")