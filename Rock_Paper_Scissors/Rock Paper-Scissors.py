import random

print("🎮 Welcome to Rock-Paper-Scissors Game!")

# Score variables
user_score = 0
computer_score = 0

# Game loop
while True:
    print("\nChoose one: rock, paper, scissors")
    user_choice = input("Your choice: ").lower()

    # Validate user input
    if user_choice not in ["rock", "paper", "scissors"]:
        print("❌ Invalid choice! Please choose rock, paper, or scissors.")
        continue

    # Computer random choice
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Game Logic
    if user_choice == computer_choice:
        print("🤝 It's a tie!")

    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("✅ You win!")
        user_score += 1
    else:
        print("❌ You lose!")
        computer_score += 1

    # Display current score
    print(f"\n📊 Score -> You: {user_score} | Computer: {computer_score}")

    # Ask if user wants to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("\nThanks for playing! Goodbye 👋")
        break
