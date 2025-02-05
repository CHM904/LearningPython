import tkinter
import tkinter.messagebox

def button_click():
    txt = entry.get()
    button.config(text=txt)

def show_msg():
    tkinter.messagebox.showinfo("資訊", "你點選按鈕了")
    tkinter.messagebox.showerror("錯誤", "這是個錯誤視窗")
    tkinter.messagebox.askretrycancel("請選擇", "要在試看看看嗎？")

root = tkinter.Tk()
root.title("第一個文字輸入欄位程式")
root.geometry("400x200")
entry = tkinter.Entry(width=20)
entry.place(x=20, y=20)

button = tkinter.Button(text="取得字串", command=button_click)
button.place(x=20, y=100)

button = tkinter.Button(text="出現訊息視窗", command=show_msg)
#button.pack()
button.place(x=20, y=160)

root.mainloop()

