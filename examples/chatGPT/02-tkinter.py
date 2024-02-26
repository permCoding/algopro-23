from tkinter import *
from tkinter import ttk
import g4f


def get_message(request):
    response = g4f.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": request}],
        n=1,
        stream=True,
        provider=g4f.Provider.You
    )
    return response

def set_msg(req):
    msg = ''.join([message for message in get_message(req)])
    editor.delete('1.0', END)
    editor.insert(END, msg)

win = Tk()
win.title("chatGPT")
win.geometry("700x400")

frame = ttk.Frame(relief='flat', padding=[28, 10])
frame.pack(pady=5)

lbl = Label(frame, font=('Consolas', 10), text='Введи свой запрос:', fg='grey')
lbl.pack(anchor=W)

ent = Entry(frame, font=('Consolas', 11), width=88)
ent.pack(anchor=W, pady=1)
req = 'Выбери лишнее: блокнот, ручка, кошка, карандаш. Поясни свой выбор.'
req = 'Какой язык программирования лучше всего использовать для создания chatGPT?'
ent.insert(END, req)


btn = Button(frame, font=('Consolas', 12), width=20, text='Get response', bg='#4499dd', command=lambda:set_msg(ent.get()))
btn.pack(side=LEFT, pady=5)

editor = Text(win, wrap = "word")
editor.configure(fg='darkgreen', bg='white', font=('Consolas', 12))
editor.pack(pady=5)

win.mainloop()

