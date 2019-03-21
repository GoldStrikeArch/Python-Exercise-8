"""
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
Remember the rules:

    Rock beats scissors
    Scissors beats paper
    Paper beats rock

"""
import time


def display_game_into():
    time.sleep(1)
    print(''' This is a rock, paper, scissor game
    The rules is simple:
    
    Rock beats scissors
    Scissors beats paper
    Paper beats rock
    
    Have fun!
    
     ''')


def first_player():
    weapon_1 = ""
    while weapon_1 != "1" and weapon_1 != "2" and weapon_1 != "3":
        time.sleep(1)
        weapon_1 = input("""Choose your weapon Player one!
        Press "1" if you want a rock
        Press "2" if you want a paper
        Press "3" if you want a scissors
        
        """)
    return weapon_1


def second_player():
    weapon_2 = ""
    while weapon_2 != "1" and weapon_2 != "2" and weapon_2 != "3":
        time.sleep(1)
        weapon_2 = input("""Choose your weapon Player Two!
        Press "1" if you want a rock
        Press "2" if you want a paper
        Press "3" if you want a scissors

        """)
    return weapon_2


def who_is_winner():
    time.sleep(1)
    weapon_one = first_player()
    weapon_two = second_player()
    print("And the winner is... ")
    time.sleep(1)
    if weapon_one == weapon_two:
        print("Its a draw!")
    elif weapon_one == "1" and weapon_two == "2":
        print("Second player won!")
    elif weapon_one == "1" and weapon_two == "3":
        print("First player won!")
    elif weapon_one == "2" and weapon_two == "1":
        print("First player won!")
    elif weapon_one == "2" and weapon_two == "3":
        print("Second player won!")
    elif weapon_one == "3" and weapon_two == "1":
        print("Second player won!")
    elif weapon_one == "3" and weapon_two == "2":
        print("First player won!")


# This function controls the flow of this app
def main_loop():
    wanna_play_again = "yes"
    while wanna_play_again == "yes" or wanna_play_again == "y" or wanna_play_again == "Yes":
        display_game_into()
        who_is_winner()
        time.sleep(1)
        print("\n\n Do you want to play again: (yes or not?)")
        wanna_play_again = input()
        print("You said " + wanna_play_again)
        time.sleep(2)
        if wanna_play_again == "yes" or wanna_play_again == "y":
            print("Ok, one more round")
        else:
            print("Good luck, see ya later! ")


main_loop()
