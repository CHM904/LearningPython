import tkinter as tk
import random

window = tk.Tk()
window.title = "Create interesting sentense"
window.geometry('320x200+1024+100')
window.config(bg='orange')


def random_nouns():
    nouns = ["cats", "dogs", "cakes", "birds", "cars", "planes"]
    return random.choice(nouns)

def random_verbs():
    verbs = ["eats", "likes", "has", "pulls", "walks", "flys"]
    return random.choice(verbs)

def button_click():
    name = name_entry.get()
    verb = random_verbs()
    noun = random_nouns()
    sentense = name + " " + verb + " " + noun
    result_label.config(text=sentense)

name_lable = tk.Label(window, text="Name:")
name_entry = tk.Entry(window)
button = tk.Button(window, text="Generate", command=button_click)
result_label =tk.Label(window, text="", fg="blue")

name_lable.pack()
name_entry.pack()
button.pack()
result_label.pack()

window.mainloop()

