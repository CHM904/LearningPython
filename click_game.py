import tkinter as tk
import time
from typing import Collection

window = tk.Tk()
window.title = "Click Game !!"
window.geometry('240x100+1024+100')

clicks = 0
start = 0
goal = 100

def button_click():
    global clicks
    global start

    if clicks == 0:
        start = time.time()
        clicks = clicks + 1
    elif clicks + 1 >= goal:
        score = time.time() - start
        label.config(text="Time: " + str(score))
        clicks = 0
    else:
        clicks = clicks + 1
    slider.set(clicks)

label = tk.Label(window)
slider = tk.Scale(window, from_=0, to=goal, orient='horizontal', length=180)
button = tk.Button(window, text="Click Me", command=button_click)

label.pack()
slider.pack()
button.pack()

window.mainloop()
