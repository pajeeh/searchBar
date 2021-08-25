from tkinter import *
import webbrowser
import time

win = Tk()
win.title("Barra de pesquisa")


def search():
    url = enterBox.get()
    webbrowser.open(url)


label1 = Label(win,
               text="URL:",
               font=("arial", 10, "bold"))

label1.grid(row=0, column=0)

enterBox = Entry(win, width=30)
enterBox.grid(row=0, column=1)

button = Button(win,
                text="Buscar",
                command=search,
                font=("arial", 12, "bold"))
button.grid(row=1, column=0, columnspan=2, pady=10)

win.mainloop()
