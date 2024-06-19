import random


def generate_number(diff):
    num = random.randint(1, diff)
    return num


def get_guess_from_user():
    num = int(input())
    return num


def compare_results(userNum, diff):
    secretNum = generate_number(diff)
    if userNum == secretNum:
        return True
    else:
        return False


def play(difficulty):
    print("Welcome to the Guess Game! \n GOOD LUCK!")
    print("Choose a number between 1 and " + str(difficulty))
    userNumber = get_guess_from_user()
    score = compare_results(userNumber, difficulty)
    if score:
        print("Congratulations! you won")
        return score
    elif not score:
        print("Sorry, you lost, the number was: " + str(userNumber))
        return score
