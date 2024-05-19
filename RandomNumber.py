from random import randint


def check_answer (user_guess, real_answer):
    if user_guess > real_answer:
        print("Too high!")
    elif user_guess < real_answer:
        print("Too low!")
    else:
        print(f"You got it! The answer was {real_answer}")


print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100!")

# Partially Updated

def main_game():
    answer = randint(1, 100)
    print(f"Answer is {answer}")
    num_lives = 0
    game_over = False
    difficulty = (input("Choose a difficulty. Type 'Easy' or 'Hard': ")).lower()
    if difficulty == 'easy':
        num_lives = 11
    elif difficulty == 'hard':
        num_lives = 6
    else:
        print("Trying to be clever are we?! Hard difficulty it is!")

    while not game_over:
        num_lives -= 1
        if num_lives == 0:
            print("You lose!")
            game_over = True
        print(f"You have {num_lives} guesses left.")
        guess = int(input("Make a guess: "))
        check_answer(guess, answer)
        if guess == answer:
            game_over = True


main_game()
