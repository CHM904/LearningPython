import tkinter as tk

window  = tk.Tk()
window.title = "Slider Tool"
window.geometry('320x200+1024+100')

def slider_change(val):
    slider_lable.config(text=str(val))

slider = tk.Scale(window, from_=0, to=100, command=slider_change)
slider_lable = tk.Label(window)

slider.pack()
slider_lable.pack()
window.mainloop()