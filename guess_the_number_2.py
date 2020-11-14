def user_choice():
    '''Function to ask user

    User gives simple answers by using integer 1, 2 or 3 to keep the game
    running

    :rtype int
    :return value in list(range(1, 4)
    '''
    rules = """Choose:
        1 - Too big
        2 - Too small
        3 - You win!\n"""
    options = [1, 2, 3]
    while True:
        try:
            answer = int(input(rules))
            if answer in options:
                break
            else:
                print("Use 1, 2 or 3 for an answer")
        except ValueError:
            print(f"Use 1, 2 or 3 for an answer.")
    return answer


def main_game():
    '''Main game

    The Python tries the guess the user's imaginary number based on answers
    received from the user.

    '''
    print("Think about a number between 0 to 1000. I will try to guess it "
          "in max. 10 attemps.\nPress 'enter' if You are ready.")
    input()

    min = 0
    max = 1001
    answer = 0
    tries = 1

    while answer != 3:
        guess = int((max - min) / 2) + min
        print(f"Guess: {guess}")
        answer = user_choice()
        tries += 1
        if answer == 1:  # computer's answer too big
            max = guess
        elif answer == 2:  # computer's answer too small
            min = guess
        if tries > 10:
            print("I guess You cheat!")
            break
    print("I win. Excellent!")


if __name__ == '__main__':
    main_game()
