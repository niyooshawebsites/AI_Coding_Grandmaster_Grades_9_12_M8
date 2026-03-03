import random

# List of numbers given for the quiz
numbers = [10, 25, 37, 42, 58, 63, 79, 84, 91, 100]

# Judge selects a random number from the list
chosen_number = random.choice(numbers)

print("Welcome to the Number Guessing Game!")
print("Guess the number from the following list:")
print(numbers)

# Loop until the correct guess
while True:
    try:
        guess = int(input("Enter your guess: "))

        # Check if guess is in the given list
        if guess not in numbers:
            print("Please choose a number from the given list!")
            continue

        if guess > chosen_number:
            print("Your guess is higher than the chosen number. Try again!")
        elif guess < chosen_number:
            print("Your guess is smaller than the chosen number. Try again!")
        else:
            print("🎉 Congratulations! You guessed the correct number!")
            break

    except ValueError:
        print("Invalid input! Please enter a valid number.")