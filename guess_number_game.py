import random
import tkinter as tk

window = tk.Tk()
window.title = "Guess number game"
window.geometry('320x200+1024+100')

max_no = 10
score = 0
rounds = 0

def button_click():
    global score
    global rounds
    try:
        guess = int(guess_box.get())
        if 0 < guess <= max_no:
            result = random.randrange(1, max_no)
            if guess == result:
                score = score + 1
                result = "Correct !!"
            else:
                result = "Wrong!!"
    except:
        result = "Invalid Input !!"

    rounds = rounds + 1
    result_label.config(text=result)
    score_label.config(text=str(score) + "/" + str(rounds))
    guess_box.delete(0, tk.END)

guess_lable = tk.Label(window, text="Enter a number from 0 to " + str(max_no))
guess_box = tk.Entry(window)
result_label = tk.Label(window)
score_label = tk.Label(window)
button = tk.Button(window, text="Guess", command=button_click)

guess_box.pack()
guess_lable.pack()
result_label.pack()
score_label.pack()
button.pack()

window.mainloop()
