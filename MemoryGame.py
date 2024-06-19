import time
import random


def generate_sequence(diff):
    list_numbers = []
    for _ in range(diff):
        list_numbers.append(random.randint(1, 100))
    return list_numbers


def user_sequence(diff):
    user_list = []
    for _ in range(diff):
        ele = int(input())
        user_list.append(ele)
    return user_list


def is_list_equal(list_1, list_2):
    return list_1 == list_2


def play(difficulty):
    print("Welcome to the Memory Game! \nAfter 1 second the list will disappear, type what you saw to win.")
    list_numbers = generate_sequence(difficulty)
    time.sleep(2)
    print(list_numbers, end='', flush=True)
    time.sleep(0.7)
    print('\r' + ' ' * len(str(list_numbers)), end='', flush=True)
    print('Type the numbers you saw: (press [ENTER] after each one) \n')
    userList = user_sequence(difficulty)
    score = is_list_equal(list_numbers, userList)
    if score:
        print('You won!')
        return score
    else:
        print('You lost! \n the numbers are: ' + str(list_numbers))
        return score
