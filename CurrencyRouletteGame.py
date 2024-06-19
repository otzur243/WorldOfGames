import random
import requests


def get_currency_rate():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url, verify=False)
    json = response.json()
    return response.json()['rates']['ILS']


def get_guess_from_user():
    while True:
        num = input()
        try:
            num = float(num)
            break
        except ValueError:
            (print("Please enter valid number"))
    return num


def play(difficulty):
    print("Welcome to the Currency Roulette game! \n GOOD LUCK!")
    amount = random.randint(1, 100)
    rate = get_currency_rate()
    amountNIS = amount * rate
    print("How much money do you think " + str(amount) + " USD is equal in NIS?")
    userAmount = get_guess_from_user()
    interval = 6 - difficulty
    difference = amountNIS - userAmount
    if abs(difference) < interval:
        print("You are correct!")
        return True
    if abs(difference) > interval:
        print("You are wrong! \nThe real amount is " + str(amountNIS) + " NIS, the rate is " + str(rate))
        return False
