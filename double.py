import tkinter as tk

window = tk.Tk()
window.title = "Python GUI program"
window.geometry('320x200')
window.config(bg='red')


def change_string():
    string_to_copy = entry.get()
    entry.insert(0, "Hello, ")

def reverse_string():
    string_to_copy = entry.get()
    string_to_copy = string_to_copy[::-1]
    entry.delete(0,tk.END)
    entry.insert(0, string_to_copy)


entry = tk.Entry(window)
button = tk.Button(window, text="Change",command=reverse_string)

entry.pack()
button.pack()
window.mainloop()

