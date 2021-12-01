import tkinter as tk

window = tk.Tk()
window.title = "Check Passoword"
window.geometry('320x200+1024+100')
window.config(bg='blue')

def check_password():
    password = "yyyyy"
    entered_password = password_entry.get()
    if password == entered_password:
        confirm_label.config(text="Correct !!")
    else:
        confirm_label.config(text="Wrong !!")


password_label = tk.Label(window, text="Enter your passowrd")
password_entry = tk.Entry(window, show="*")
button = tk.Button(window, text="Check",command=check_password)
confirm_label = tk.Label(window, fg='black')

password_label.pack()
password_entry.pack()
button.pack()
confirm_label.pack()

window.mainloop()
