from tkinter import *

def set_msg():
    msg['text'] = ent.get()

win = Tk()
win.title("METANIT.COM")
win.geometry("600x300")
font = ('Consolas', 14)

lbl = Label(win, font=font, width=16, text='Имя файла:', fg='grey')
lbl.pack(pady=5)

ent = Entry(win, font=font, width=16)
ent.pack(pady=5)

msg = Message(win, font=font, width=300, text='Поле для вывода ответа', fg='grey')
msg.pack(pady=5)

btn = Button(win, font=font, width=20, text='Save to file', bg='#4499dd', command=set_msg)
btn.pack(pady=5)
 
win.mainloop()
