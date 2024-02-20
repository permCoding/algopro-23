from tkinter import *

def gen():
    print(123)

win = Tk()
win.title("labrab-01")
win.geometry("600x300")
font = ('Consolas', 16)

btn = Button(win, font=font, width=32, \
    fg='yellow', bg='darkgreen', \
    text='Сгенерировать', command=gen)
btn.pack(pady=10)

win.mainloop()

"""
1)
сгенерировать 10 случайных чисел от 100 до 999
и сохранить в файл gen.txt
121 455 666 754 123 ...
"""
