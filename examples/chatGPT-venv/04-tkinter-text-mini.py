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
win.geometry("800x600")

frame = ttk.Frame(relief='flat', padding=[28, 10])
frame.pack(pady=5)

lbl = Label(frame, font=('Consolas', 10), text='Введи свой запрос:', fg='darkgrey')
lbl.pack(anchor=W)

ent = Text(frame, wrap = "word", width=72, height=3)
ent.configure(fg='darkgreen', bg='#CCEEDD', font=('Consolas', 12))
req = 'Выбери лишнее: блокнот, ручка, кошка, карандаш. Поясни свой выбор.'
ent.insert(END, req)
ent.pack(anchor=W, pady=1)


frameB = ttk.Frame(relief='flat', padding=[28, 10])
frameB.pack(pady=5)

btn = Button(frameB, font=('Consolas', 12), width=20, bg='#4499dd', 
             text='Get response', 
             command=lambda:set_msg(ent.get("1.0",END)))
btn.pack(side=LEFT, padx=5)

btn_mini = Button(frameB, font=('Consolas', 12), width=20, bg='#4499dd', 
                  text='Сократи текст', 
                  command=lambda:set_msg(editor.get("1.0",END) + ' сократи этот текст'))
btn_mini.pack(side=LEFT, padx=5)


editor = Text(wrap = "word")
editor.configure(fg='darkgreen', bg='white', font=('Consolas', 12))
editor.pack(pady=10)

win.mainloop()

