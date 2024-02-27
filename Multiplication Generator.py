# Multiplication Tables Generation

# Welcome message
print("Welcome to the Multiplication Tables generator!")

# Read user name
user_name = input("Please enter your name: ")

# Accept input (multiplicand, multiplier, times) from user
multiplicand = int(input(user_name + " please enter the number you want to begin to generate the multiplication table from:  "))
multiplier = int(input("Please enter the number you want to use to generate the multiplication table: "))
times = int(input("Please enter how many times you want to show the multiplication table: "))

# Confirm user input
print("You have entered: Multiplicand:", multiplicand, "Multiplier:", multiplier, "Times:", times)

# Process input and display output
print("Multiplication Table for", multiplicand, "x", multiplier, ":\n")
for i in range(1, times+1):
    result = multiplicand * multiplier
    print(multiplicand, "x", multiplier, "=", result)
    multiplicand += 1

# Thank you message
print("\nThank you for using the Multiplication Tables generator!")