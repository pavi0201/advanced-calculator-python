import math

def show_menu():
    print("\n ..Advanced Calculator..")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (x^y)")
    print("6. Square Root")
    print("7. Sine (sin)")
    print("8. Cosine (cos)")
    print("9. Tangent (tan)")
    print("10. Logarithm (log)")
    print("11. Factorial")
    print("12. Exit")


def calculator():
    while True:
        show_menu()
        choice = int(input("Enter your choice: "))

        if choice == 12:
            print("Exiting Calculator...")
            break

        # Basic operations
        if choice in [1, 2, 3, 4, 5]:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == 1:
                print("Result:", a + b)
            elif choice == 2:
                print("Result:", a - b)
            elif choice == 3:
                print("Result:", a * b)
            elif choice == 4:
                if b == 0:
                    print("Error! Division by zero.")
                else:
                    print("Result:", a / b)
            elif choice == 5:
                print("Result:", a ** b)

        # Advanced operations
        elif choice == 6:
            num = float(input("Enter number: "))
            print("Result:", math.sqrt(num))

        elif choice == 7:
            num = float(input("Enter angle in degrees: "))
            print("Result:", math.sin(math.radians(num)))

        elif choice == 8:
            num = float(input("Enter angle in degrees: "))
            print("Result:", math.cos(math.radians(num)))

        elif choice == 9:
            num = float(input("Enter angle in degrees: "))
            print("Result:", math.tan(math.radians(num)))

        elif choice == 10:
            num = float(input("Enter number: "))
            print("Result:", math.log(num))

        elif choice == 11:
            num = int(input("Enter integer: "))
            print("Result:", math.factorial(num))

        else:
            print("Invalid choice! Try again.")


# Run the calculator
calculator()
