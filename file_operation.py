from io import open

with open('test.txt', 'r') as fin:
    for line in fin:
        print(line, end='')


with open('test.txt', 'r') as openfile:
    with open('test_w.txt', "w") as writefile:
        for line in openfile:
            print (line, end='')
            writefile.write(line)

with open('test.txt', 'r') as openfile, open('test_w.txt', 'a') as writefile:
    for line in openfile:
        print(line, end="")
        writefile.write(line)

