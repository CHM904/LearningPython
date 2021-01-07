# This is main code for Python learning

import math_cal
import game
import a1_string
import a2_list


def print_title():
    print("1. String Operation")
    print("2. List Operation")
    print("3. Game Operation")
    print("4. Math Operation")


if __name__ == '__main__':

    print_title()
    select_value = int(input("Please select your operation:"))

    if select_value == 1:
        a1_string.string_operation(input("What is your testing string: "))
    elif select_value == 2:
        a2_list.list_operation()
    elif select_value == 3:
        game.game_start()
    elif select_value == 4:
        math_cal.print_mathtable()
        math_cal.Guess_Number(50)
    else:
        print("Your operation nnot support. Bye!!")
