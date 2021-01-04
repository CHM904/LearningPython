# This is a learning code for Python

import math_cal
import game
import a1_string


def greeting(str_name):
    # print response
    print(f'Hi, {str_name}, How are your today?')
    print()


def print_title():
    print("1. Red")
    print("2. Blue")
    print("3. Yellow")
    print("4. Purple")


if __name__ == '__main__':

    str_username = input("What's your name: ")
    greeting(str_username)

    str_teststr = input("What is your string:")
    testing_string(str_teststr)


    #game.game_start()

    #math_cal.print_mathtable()

    #math_cal.Guess_Number(50)

    #int_result = 45
    #print(bin(int_result))
    #print(oct(int_result))
    #print(hex(int_result))


    #print_title()
    #Choice = int(input("What is your color?"))

    #if (Choice == 1):
    #    response('Red')
    #elif (Choice == 2):
    #    response('Blue')
    #elif (Choice == 3):
    #    response('Yellow')
    #else:
    #    response('Wrong number')



    #print("Enter your age")
    #int_age = int(input('Enter your age'))

    #for count in range(1, int_age, 1):
    #    print("You are old!!" if int_age > 40 else "You are young!!")








