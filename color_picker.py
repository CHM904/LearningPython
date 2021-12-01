import tkinter as tk

window = tk.Tk()
window.geometry('+1024+100')

def slider_update(val):
    red = red_slider.get()
    green = green_slider.get()
    blue = blue_slider.get()

    selected_color = "#%02x%02x%02x" % (red, green, blue)
    canvas.config(bg=selected_color)
    hex_text.delete(0, tk.END)
    hex_text.insert(0, selected_color)

red_slider = tk.Scale(window, from_=0, to=255, command=slider_update)
green_slider = tk.Scale(window, from_=0, to=255, command=slider_update)
blue_slider = tk.Scale(window, from_=0, to=255, command=slider_update)

canvas = tk.Canvas(window, width=200, height=200)
hex_text = tk.Entry(window)

red_slider.grid(row=1, column=1)
green_slider.grid(row=1, column=2)
blue_slider.grid(row=1, column=3)
canvas.grid(row=2, column=1, columnspan=3)
hex_text.grid(row=3, column=1, columnspan=3)

window.mainloop()