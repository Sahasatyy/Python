#Simple error handling demonstration
try: 
    age = int(input("Enter your age: "))
    guess = age - 10
    print(f"10 years before you were {guess} years old")
except:
    print("Invalid input! **SOMETHING WENT WRONG**")