# while True:
#     inp = int(input("Enter a number"))
#     print(inp)
#     if inp < 0:
#         break
# print("Negative number detected")

#Number guessing game:
from random import randint
low, high = 1, 50
secret_number = randint(low, high) 
hint = ''

while True:
    guess = input("Enter a number between " + str(low) + " and " + str(high) + ": ") #str() was used to convert int into str for easy concatenation
    number = int(guess)
    if number > secret_number:
        hint = print("hint: A little lower than that!")
    elif number < secret_number:
        hint = print("hint: A little higher than that!")
    else:
        break
print("yayyy!! You guessed it correct. It was " + str(secret_number))