from tkinter import *
import requests

def set_msg(url):
    res = requests.get(url)
    res.encoding = 'utf8'
    editor.delete('1.0', END)
    editor.insert(END, res.text)

win = Tk()
win.title("METANIT.COM")
win.geometry("600x600")
font = ('Consolas', 14)

lbl = Label(win, font=font, width=16, text='url-адрес файла:', fg='grey')
lbl.pack(pady=5)

ent = Entry(win, font=('Consolas', 10), width=42)
ent.pack(pady=5)
url = 'https://pcoding.ru/txt/labrab04-3.txt'
ent.insert(END, url)

btn = Button(win, font=font, width=20, text='Get file', bg='#4499dd', command=lambda:set_msg(ent.get()))
btn.pack(pady=5)

editor = Text(wrap = "word")
editor.configure(fg='darkgreen', bg='white', font=('Consolas', 12))
editor.pack(pady=5)

win.mainloop()

"""
Вывести на экран названия языков программирования по возрастанию
Данные находятся в файле https://pcoding.ru/txt/labrab04-3.txt
"""