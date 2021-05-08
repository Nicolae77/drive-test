while True:
    car = input("To check your age type 'y' to exit 'e':\n")
    if car == 'y':
        age = int(input("How old are you?"))
        if age > 18:
            print(f"You can drive at age {age}")
        else:
            print("You are to young for driving a car.")
    elif car == 'e':
        print("You have finished checking. ")
        break
    else:
        print("Type 'y' for checking and 'e' for 'exit'")
        break