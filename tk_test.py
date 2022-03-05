from tkinter import Tk, Text

def alertDayInfo():
    s = 'Hello World'
    #alert('Day info', s);
    tk_show(s, 'Today info')

def tk_show(s, title="Month calendar"):
    root = Tk()
    root.geometry("600x140")
    root.resizable(True, True)
    root.title(title)
    text = Text(root, height=8)
    text.pack()
    text.insert('1.0', s)
    #root.mainloop()
    
#alertDayInfo()

from tkinter import *
# https://likegeeks.com/python-gui-examples-tkinter-tutorial/

def clicked():
    print(selected.get())    
    
window = Tk()
window.geometry("600x140")
window.title("Welcome to LikeGeeks app")

selected = IntVar()
btn = Button(window, text="Click Me", command=clicked)
rad1 = Radiobutton(window,text='First', value=1, variable=selected)
rad2 = Radiobutton(window,text='Second', value=2, variable=selected)
rad3 = Radiobutton(window,text='Third', value=3, variable=selected, activebackground='red',bg='grey') 
rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)
btn.grid(column=1, row=1)
rad3.select()  # https://www.tutorialspoint.com/python/tk_radiobutton.htm


window.mainloop()

