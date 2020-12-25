import random


def print_mathtable():
    print("  |", end='')

    for k in range(1, 10):
        print('{0:3d}'.format(k), end= '')

    print()
    print('-' * 32)

    for x in range(1, 10):
        print(x, "|", end="")

        for y in range(1,10):
            print("{0:3d}".format(x*y), end="")

        print()


def Guess_Number(int_MaxNumber):
    print(" Please guess a number between 1 to {0}".format(int_MaxNumber))

    int_GuessNumber = 0
    int_AnswerNumber = random.randint(1, int_MaxNumber)

    while int_GuessNumber != int_AnswerNumber:
        int_GuessNumber = int(input("What's your guess number: "))

        if int_GuessNumber == int_AnswerNumber:
            print("You are right!! The number is ", int_AnswerNumber)
        elif int_GuessNumber > int_AnswerNumber:
            print("The number is lower!!")
        else:
            print("The number is higher!!")

