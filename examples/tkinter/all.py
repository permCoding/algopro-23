from tkinter import *
from tkinter import ttk

def set_msg():
    lbl['text'] += '+'
    msg['text'] = ent.get()
    ent.delete(0,END)
    ent.insert(0,"- - -")
    if pb['value'] < 100: pb['value'] += 10

def set_click():
    rb_num = rbs.get()
    lbl['text'] = f'rb_num = {rb_num}'
    
win = Tk()
win.title("METANIT.COM")
win.geometry("600x300")
font = ('Consolas', 14)

lbl = Label(win, font=font, width=16, text='Имя файла:', fg='grey')
lbl.pack(pady=5)

ent = Entry(win, font=font, width=22)
ent.pack(pady=5)

msg = Message(win, font=font, width=300, text='Поле для вывода ответа', fg='grey')
msg.pack(pady=5)

btn = Button(win, font=font, width=20, text='Save to file', bg='#4499dd', command=set_msg)
btn.pack(pady=5)

pb = ttk.Progressbar(win, orient="horizontal", length=250, mode="determinate"); pb.pack()


frameRB = ttk.Frame(relief='flat', padding=[28, 10])
frameRB.pack()

rbs = IntVar()
rb0 = Radiobutton(frameRB, text='Камень', value=0, variable=rbs, command=set_click)
rb1 = Radiobutton(frameRB, text='Ножницы', value=1, variable=rbs, command=set_click)
rb2 = Radiobutton(frameRB, text='Бумага', value=2, variable=rbs, command=set_click)
rb0.pack(anchor=W); rb1.pack(anchor=W); rb2.pack(anchor=W)


win.mainloop()
