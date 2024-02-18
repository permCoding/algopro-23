from tkinter import *
from random import randint
from tkinter import ttk

font = ("Consolas", 14)

win = Tk()
win.title("Камень, ножницы, бумага")
win.geometry("600x300+500+200")
win.resizable(False, False)

def get_click():
    rb_num = rbs.get()
    lbl['text'] = str(rb_num)
def set_click():
    rb_num = rbs.get()
    lbl['text'] = str(rb_num)

for c in range(2): win.columnconfigure(index=c, weight=1)
for r in range(2): win.rowconfigure(index=r, weight=1)  # это пропорция по фрейму

frameH = ttk.Frame(relief='flat', padding=[28, 10])
frameH.grid(row=0, column=0)

rbs = IntVar()
rb0 = Radiobutton(frameH, text='Камень', value=0, variable=rbs, command=set_click)
rb1 = Radiobutton(frameH, text='Ножницы', value=1, variable=rbs, command=set_click)
rb2 = Radiobutton(frameH, text='Бумага', value=2, variable=rbs, command=set_click)
rb0.pack(anchor=W); rb1.pack(anchor=W); rb2.pack(anchor=W)


frameC = ttk.Frame(relief='flat', padding=[28, 10])
frameC.grid(row=0, column=1)

btn_get = Button(frameC, text="get", width=20, font=font, command=get_click)
btn_get.pack()

lbl = Label(frameC, text="0", font=font); lbl.pack()


win.mainloop()