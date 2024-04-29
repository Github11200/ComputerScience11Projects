import random
import os.path


def check_who_won(user_input, computer_input):
    return (user_input == "ROCK" and computer_input == "SCISSORS") or (user_input == "PAPER" and computer_input == "ROCK") or (user_input == "SCISSORS" and computer_input == "PAPER")


def tied(user_input, computer_input):
    return user_input == computer_input


def file_exists(file_path):
    return os.path.isfile(file_path)


file_path = "./scores.txt"
choices = ["ROCK", "PAPER", "SCISSORS"]
is_tie = True
continue_playing = True
user_score = 0
computer_score = 0
f = None

if file_exists(file_path=file_path):
    f = open(file_path, "r")
    if f.read() != "":
        f.seek(0)
        user_score = int(f.readline())
        computer_score = int(f.readline())
    f.close()
else:
    f = open(file_path, "x")
    f.close()

while continue_playing:
    is_tie = True
    while is_tie:
        user_input = int(
            input("Please choose between Rock (1), Paper (2), or Scissors(3): "))

        while user_input < 1 or user_input > 3:
            user_input = int(
                input("Please enter again, choose between Rock (1), Paper (2), or Scissors(3): "))

        user_input = choices[user_input - 1]
        computer_input = choices[random.randrange(0, 3)]

        print(f"\nYou inputted: {user_input}")
        print(f"The computer inputted: {computer_input}\n")

        if tied(user_input, computer_input):
            print("It is a TIE! Please input again")
            print(
                "\n================================================================================\n")
            continue
        elif check_who_won(user_input, computer_input):
            print("You won!")
            user_score += 1
        else:
            print("The computer won!")
            computer_score += 1

        print(f"\nYour score: {user_score}")
        print(f"Computer score: {computer_score}")

        is_tie = False

    continue_playing = int(input(
        "\nWould you like to continue playing (0 -> no, 1 -> yes)?: "))

f = open(file_path, "w")
f.write(str(user_score) + "\n")
f.write(str(computer_score))
f.close()

print("\nBye!")
