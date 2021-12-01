
colors = ["red", "yellow", "blue", "purple"]
anaimals = ["dog", "cat", "chicken", "tiger", "lion"]
mix_anaimals = []

for x in colors:
    for y in anaimals:
        mix_anaimals += [x + " " +y]

print(mix_anaimals)

for x in range(1, 10):
    for y in range(1, 10):
        if (x>0 and y>0):
            print (str(x) + " * " + str(y) + " = " + str(x*y))

x = 1
y = 1
while x<10:
    while y<10:
        print (str(x) + " x " + str(y) + " = " + str(x*y))
        x += 1
        y += 1
