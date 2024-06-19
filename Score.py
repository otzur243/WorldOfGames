import Utils


def add_score(difficulty):
    difficulty = int(difficulty)
    score = difficulty * 3 + 5
    return score


def read_score():
    try:
        with open("scores.txt", "a") as file:
            pass
        with open("scores.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return 0


def update_score(difficulty, won):
    current_score = read_score()
    if won:
        points_gained = add_score(difficulty)
        new_score = int(current_score) + int(points_gained)
        write_score(new_score)
        return new_score
    else:
        return current_score


def write_score(score):
    with open("scores.txt", "w") as file:
        file.write(str(score))



