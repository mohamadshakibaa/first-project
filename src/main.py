from src.game_logic.hint_generator import provide_hint
from src.game_logic.number_generator import random_number
from src.game_logic.scores import Scorer
from src.utils.input_validator import get_valid_input


def main():
    random_num = random_number(1, 100)
    score = Scorer()

    while True:
        guess_number = get_valid_input(1, 100)
        if guess_number == random_num:
            print(f"Congratulations!! Your guess number is correct. Your finall score: {score.get_score()}")
            break
        else :
            hint = provide_hint(guess_number, random_num)
            print (hint)
            score.decrement_score()

if __name__=="__main__":
    main()
