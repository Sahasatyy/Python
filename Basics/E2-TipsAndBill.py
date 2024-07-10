#Program to calculate the total amount in a bill including tips and no of share per person.

Tamount = int(input("Enter the total paying amount: "))
Tshare = int(input("Enter the no of person for splitting the bill: "))
Tip = input("Would you like to give a tip ? yes or no: ").lower()

if Tip == ("yes"):
    Tipamt = int(input("Enter the percentage 10%, 15%, or 20% (*DON'T INCLUDE PERCENTAGE SIGN): "))
    Tamount2 = (Tamount * Tipamt/100) + Tamount
    print("Your total bill is Rs " + str(Tamount2) + ".")
    ShareAmt2 = (Tamount2 / Tshare)
    print("Each person should pay RS. " + str(ShareAmt2) + ".")
else:
    print("Your total bill is Rs " + str(Tamount) + ".")
    ShareAmt = Tamount / Tshare
    print("Each person should pay RS. " + str(ShareAmt) + ".")
