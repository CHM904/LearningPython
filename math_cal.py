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
    print(" Try to guess a number between 1 to {0}".format(int_MaxNumber))
    print('-' * 50)
    print()

    int_GuessNumber = -1
    int_AnswerNumber = random.randint(1, int_MaxNumber)
    int_Count = 0

    while int_GuessNumber != int_AnswerNumber:
        int_Count = int_Count + 1

        int_GuessNumber = int(input("{0} time to guess a number between 1 to {1}:".format(int_Count, int_MaxNumber)))

        if int_GuessNumber == int_AnswerNumber:
            print("After {0} time, you got right number: {1} ".format(int_Count, int_AnswerNumber))
        elif int_GuessNumber > int_AnswerNumber:
            print("Wrong number!! It is lower!!")
        else:
            print("Wrong number!! It is higher!!")

