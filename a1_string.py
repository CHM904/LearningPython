

def string_operation(str_Value):
    print("The input string is \"{0}\"".format(str_Value))
    print("This string length is {0}".format(len(str_Value)))
    print("-"*len(str_Value))
    print("First character: {0}".format(str_Value[0]))
    print("Last character: {0}".format(str_Value[-1]))
    print("First 3 characters: {0}".format(str_Value[0:3]))
    print("First 4 characters with 2 steps: {0}".format(str_Value[0:8:2]))

    print("The original string print by character.")
    count = 0
    for count in range(len(str_Value)):
        print(str_Value[count], end="")





