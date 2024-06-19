import GuessGame, CurrencyRouletteGame, MemoryGame, Score


def welcome(name):
    welcomeStr = ("Hello " + name + " and welcome to the World of Games (WoG).\n "
                                    "Here you can find many cool games to play")
    return welcomeStr


def num_insert_n_check():
    while True:
        num = input()
        try:
            num = int(num)
            break
        except ValueError:
            (print("Please enter valid number"))
    return num


def load_game():
    print("Choose what game would you like to play: \n 1. Memory game \n"
          " 2. Guess game \n 3. Currency roulette ")
    game = num_insert_n_check()
    while game not in (1, 2, 3):
        print("Please enter a valid number between 1 to 3")
        game = num_insert_n_check()
    print("Please choose game difficulty from 1 to 5:")
    difficulty = num_insert_n_check()
    while difficulty not in (1, 2, 3, 4, 5):
        print("Please enter a valid number between 1 to 5")
        difficulty = num_insert_n_check()
    if game == 1:
        won = MemoryGame.play(difficulty)
        Score.write_score(Score.update_score(difficulty, won))
    elif game == 2:
        won = GuessGame.play(difficulty)
        Score.write_score(Score.update_score(difficulty, won))
    elif game == 3:
        won = CurrencyRouletteGame.play(difficulty)
        Score.write_score(Score.update_score(difficulty, won))
    else:
        print("Invalid game. Please try again.")

    if input("would you like to play again? (y/n) ") == "y":
        load_game()
