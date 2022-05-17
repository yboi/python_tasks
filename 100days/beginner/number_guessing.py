from random import randint
from art import logo3

print(logo3)
print("Welcome to the Number Guessing Game")
print("I'm thinking of a number 1 and 100")

random = randint(1, 100)


def game():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        attempts = 10
        print("You have 10 attempts")
    else:
        attempts = 5
        print("You have 5 attempts")
    while attempts != 0:
        for count_attempts in range(attempts):
            quess = int(input("Make a guess: "))
            if random > quess:
                print("To low")
            elif random < quess:
                print("To high")
            else:
                return print(f"You got it! Answer was {random}.")
            attempts -= 1
            print(f"You have {attempts} attempts remaining to guess a number")

    print(f"You have {attempts} attempts remaining to guess a number: number was {random}")


game()
