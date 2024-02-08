import random
def guess_game():
    r = random.randint(1, 10)
    p=int(input(f"Enter a number between 1 and 10: "))
    if r==p:
        print("your guess is correct")
    else:
        print("your guess is wrong")
    guess_game()
guess_game()
