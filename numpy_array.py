import numpy as np
import matplotlib.pyplot as plt
import random as rd

from numpy import random

score1 = np.array([[80, 89, 77, 90, 84, 92], [85, 82, 80, 95, 88, 96]])
score2 = np.array([[83, 85, 72, 95, 85, 91], [81, 89, 85, 91, 82, 93]])

for i in range(2):
    for j in range(6):
        print(score1[i][j], end=' ')
    print()

print()

for i in range(2):
    for j in range(6):
        print(score2[i][j], end=' ')
    print()

print("==============================")

ave = (score1+score2)/2

for i in range(2):
    for j in range(6):
        print(ave[i][j], end=' ')
    print()

def get_score(total, interval):
    for i in range(total):
        number = rd.randint(1, interval)
        score.append(number)

def statistics(interval):
    for i in range(1, interval+1):
        number = score.count(i)
        times.append(number)

total = 10000
interval = 10
score = []
times = []

get_score(total, interval)
statistics(interval)

for i in range(10):
    print(times[i])

x=np.arange(10)
width= 0.6
plt.bar(x, times, width, color='blue')
plt.ylabel('Total students in each interval')
plt.title('Ten thounds people score')
plt.xticks(x, ('0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80-89', '90-100'))
plt.yticks(np.arange(0, 1200, 50))
plt.show()


