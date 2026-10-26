import trace

print(
    "Select one of the three games: 1. Treasure Game, 2. Roller Coaster, 3. Even Or Odd, 4. BMI Calculator, 5. Check if Leap Year, 6. Order a pizza, 7. Love Calculator"
)
choice = int(input("Your chosen game:"))


match choice:
    case 1:
        print("Treasure Game")
    case 2:
        height = int(input("How tall are you in cm?"))
        bill = 0
        if height >= 120:
            print("You are allowed to ride the roller coaster")
            print(
                "How old are you? Adult Tickets: 12$, Teen Tickets: 10$, Child Tickets: 7$"
            )
            age = int(input("Age: "))
            if age > 18:
                print("You have bought an adult ticket -12$")
                bill = 12
            elif age < 18 and age > 12:
                print("You have bought an teen ticket -10$")
                bill = 10
            else:
                print("You have bought an child ticket -7$")
                bill = 7
            wantphoto = input("Do you want a photo? Y or N: ")
            if wantphoto == "Y":
                bill += 3
            print(f"Your final bill is: ${bill}")
        else:
            print("You are not allowed to ride the roller coaster")
    case 3:
        print("\n Even Or Odd:")
        number = int(input("Which number do you choose?"))
        if number % 2 == 0:
            print("Even number")
        else:
            print("Odd number")
    case 4:
        print("BMI Calculator")
        weight = int(input("Weight in kg: "))
        height = int(input("Height in cm: ")) / 100
        bmi = int(weight / (height * height))
        print(f"Your BMI is {bmi}")
        if bmi < 18.5:
            print("Underweight")
        elif bmi < 25:
            print("Normal weight")
        elif bmi < 30:
            print("Obesity")
        else:
            print("Severe obesity")
    case 5:
        print("Leap Year")
        year = int(input("Which year do you choose?"))
        isleap = False
        if year % 4 == 0:
            isLeap = True
        if year % 100 == 0:
            isLeap = False
        if year % 400 == 0:
            isLeap = True
        if isLeap:
            print("Leap year")
        else:
            print("Not a leap year")
    case 6:
        print("Order a Pizza")
        size = input("Small, Medium or Large: ")
        add_pepperoni = input("Want pepperoni? Y or N: ")
        extra_cheese = input("Want extra cheese? Y or N: ")
        bill = 0
        if size == "Small":
            bill += 15
        elif size == "Medium":
            bill += 20
        else:
            bill += 25
        if add_pepperoni == "Y":
            if size == "Small":
                bill += 2
            else:
                bill += 3
        if extra_cheese == "Y":
            bill += 1
        print(f"Your final bill is: ${bill}")
    case _:
        print("Invalid choice")
