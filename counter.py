import tkinter

count = 0

def count_up():
    global count
    count = count + 1
    label["text"] = count
    root.after(1000, count_up)

root = tkinter.Tk()
label = tkinter.Label(font=("Times New Roman", 80))
label["text"] = count
label.pack()

root.after(1000, count_up)
root.mainloop()