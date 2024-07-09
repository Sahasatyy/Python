age = int(input("Enter your age: "))
match age:
    case 18:
        print("You can get in as this is your last year")
    case 17:
        print("You can get in but for 1 more year")
    case 16:
        print("You can get in but for 2 more years")
    case 15:
        print("You can get in but for 3 more years")
    case _ if age > 18:
        print("You cannot get in as you are older")
    case _ if age < 18:
        print("You cannot get in as you are younger")
    