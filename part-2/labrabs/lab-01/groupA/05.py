from tkinter import *

def gen():
    filename = ent1.get()
    msg['text'] = filename

win = Tk()
win.title("labrab-01")
win.geometry("600x300")
win.configure()
font = ('Consolas', 16)

lbl1 = Label(win, font=font, width=32, text='Имя файла:')
lbl1.pack(pady=10)

ent1 = Entry(win, font=font, width=32)
ent1.pack(pady=10)

msg = Message(win, font=font, width=336, text="- - - - - - - -")
msg.pack(pady=10)

btn = Button(win, font=font, width=32, fg='#FFD700', bg='CadetBlue', text='Сгенерировать', command=gen)
btn.pack(pady=10)

win.mainloop()
