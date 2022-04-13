import random
from data import data
from logo import vs, logo


def pick_number():
    """Take a random data from dictionary data and return it"""
    return random.choice(data)


def format_data(accounts):
    """Take data from dictionary and format it Name Description Country"""
    name = accounts["name"]
    description = accounts["description"]
    country = accounts["country"]

    return f"{name} a {description} from {country}"


def check_score(guess, a_player_count, b_player_count):
    """Compare Player 1 and Player 2 follower score and return the correct guess"""
    if a_player_count > b_player_count:
        return guess == "a"
    else:
        return guess == "b"


def game():
    """Game HighLow"""

    print(logo)
    player_b = pick_number()
    score = 0
    game_is_over = False

    while not game_is_over:
        player_a = player_b
        player_b = pick_number()

        while player_a == player_b:
            player_b = pick_number()

        print(f"Compare A : {format_data(player_a)}")
        print(vs)
        print(f"Compare B : {format_data(player_b)}")

        guess = input("Who has more followers? A or B: ").lower()

        # Format and get playerA and playerB follower count.
        a_player_count = player_a["follower_count"]
        b_player_count = player_b["follower_count"]

        # Check if the guess is the correct one.
        is_correct = check_score(guess, a_player_count, b_player_count)
        
        if is_correct:
            score += 1
            print(f"You are right! Your score: {score}")
        else:
            game_is_over = True
            print(f"You are wrong! Your final score {score}")

