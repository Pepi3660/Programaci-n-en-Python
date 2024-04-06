import os

# Function to input two integers from the user
def enter_numbers():
    while True:
        try:
            num1 = int(input("Enter the first number: "))  # Request the first number
            num2 = int(input("Enter the second number: "))  # Request the second number
            return num1, num2
        except ValueError:
            print("Error: Please enter only integers.")  # Exception handling if a non-integer is entered

# Function to clear the screen according to the operating system
def clear_screen():
    if os.name == 'nt':  # If it's Windows
        os.system('cls')
    else:
        os.system('clear')  # For other operating systems

while True:
    print("\n\t\tOPTIONS MENU: \n")
    print("\t\t1. Sum")
    print("\t\t2. Subtract")
    print("\t\t3. Multiplication")
    print("\t\t4. Division")
    print("\t\t5. Exit")

    option_str = input("\n\t\tOption: ")  # Request the option from the user
    try:
        option = int(option_str)  # Try to convert the option to an integer
    except ValueError:
        option = 0  # If conversion fails, assign 0 as the option

    clear_screen()  # Clear the screen after the user enters the option

    # Validation of the option entered by the user
    if option not in range(1, 6):
        print("\n\t\tERROR: INVALID OPTION")  # Error message if an invalid option is entered
        input("Press Enter to continue...")
        clear_screen()
        continue  # Go back to the beginning of the loop to display the menu again

    # Perform the operation corresponding to the option selected by the user
    if option == 1:
        num1, num2 = enter_numbers()
        print("\n\t\tThe sum of ", num1, "+", num2, "=", num1 + num2)
    elif option == 2:
        num1, num2 = enter_numbers()
        print("\n\t\tThe subtraction of ", num1, "-", num2, "=", num1 - num2)
    elif option == 3:
        num1, num2 = enter_numbers()
        print("\n\t\tThe product of ", num1, "*", num2, "=", num1 * num2)
    elif option == 4:
        num1, num2 = enter_numbers()
        if num2 != 0:
            print("\n\t\tThe quotient of ", num1, "/", num2, "=", num1 / num2)
        else:
            print("\n\t\tERROR: Division by zero\n")
    elif option == 5:
        print("\n\n\t\tGOODBYE!!\n\n")
        break  # Exit the while loop if the user chooses to exit

    input("Press Enter to continue...")  # Wait for the user to press Enter to continue
    clear_screen()  # Clear the screen before displaying the menu again