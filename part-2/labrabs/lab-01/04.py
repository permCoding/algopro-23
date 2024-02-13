from tkinter import *

def gen():
    filename = ent1.get()
    print(filename)

win = Tk()
win.title("labrab-01")
win.geometry("600x300")
win.configure(bg='grey')
font = ('Consolas', 16)

lbl1 = Label(win, font=font, width=32, text='Имя файла:')
lbl1.pack(pady=10)
ent1 = Entry(win, font=font, width=32)
ent1.pack(pady=10)

lbl2 = Label()
lbl2.pack(pady=10)
ent2 = Entry()
ent2.pack(pady=10)

btn = Button(win, font=font, width=32, fg='#FFD700', bg='CadetBlue', text='Сгенерировать', command=gen)
btn.pack(pady=10)

win.mainloop()

"""
1)
сгенерировать 10 случайных чисел от 100 до 999
и сохранить в файл gen.txt
121 455 666 754 123 ...
"""
