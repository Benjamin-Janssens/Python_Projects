# Welcome message to the game
print("Welcome to the Rock Paper Scissors game!")

# Read players' names
while True:
    player1_name = input("Player 1, please enter your name: ")
    player2_name = input("Player 2, please enter your name: ")
    if player1_name and player2_name:  # Check if both names are entered
        break
    else:
        print("Please enter a name for both players.")

# while Loop to handle multiple rounds
while True:
    # Accept input choices from both players with error handling
    while True:
        try:
            player1_choice = input(player1_name + ", please choose Rock, Paper, or Scissors: ").lower().strip()
            if player1_choice in ("rock", "paper", "scissors"):
                break
            else:
                print("Invalid choice. Please choose Rock, Paper, or Scissors.")
        except ValueError:  # Handle non-string input
            print("Invalid input. Please enter a valid choice.")

    while True:
        try:
            player2_choice = input(player2_name + ", please choose Rock, Paper, or Scissors: ").lower().strip()
            if player2_choice in ("rock", "paper", "scissors"):
                break
            else:
                print("Invalid choice. Please choose Rock, Paper, or Scissors.")
        except ValueError:  # Handle non-string input
            print("Invalid input. Please enter a valid choice.")

    # Check for a tie
    if player1_choice == player2_choice:
        print("It's a tie!")

    # Check for all possibilities and output score
    elif player1_choice == "rock":
        if player2_choice == "scissors":
            print(player1_name + " wins!")
        else:
            print(player2_name + " wins!")
    elif player1_choice == "paper":
        if player2_choice == "rock":
            print(player1_name + " wins!")
        else:
            print(player2_name + " wins!")
    elif player1_choice == "scissors":
        if player2_choice == "paper":
            print(player1_name + " wins!")
        else:
            print(player2_name + " wins!")

    # Ask if players want to play another round
    play_again = input("\nDo you want to play another round? (yes/no): ")
    if play_again.lower().strip() != "yes":
        break

# Thank you message
print("Thank you for playing the Rock Paper Scissors game!")
