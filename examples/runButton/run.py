from tkinter import *
from random import randint as rnd
from tkinter import messagebox

def btnNoMove(event):
    newX, newY = rnd(0, w-150), rnd(0, h-50)
    btnNo.place(x=newX, y=newY)

def yes():
    messagebox.showinfo('+++', "Спасибо )))")
    quit()

win = Tk()
w, h = 900, 600
win.geometry(f"{w}x{h}")
win.title("Ответь на вопрос")
win.resizable(width=False, height=False)

lbl = Label(win, text="Довольны ли Вы своей зарплатой?", font='24').pack()
btnYes = Button(win, text="Yes", width=24, height=2, command=yes)
btnYes.place(x=250, y=100)
btnNo = Button(win, text="No", width=24, height=2)
btnNo.place(x=500, y=100)

btnNo.bind('<Enter>', btnNoMove)

win.mainloop()
