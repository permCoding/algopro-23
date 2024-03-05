from tkinter import *


def set_msg():
    filename = ent.get()  # получили имя файла
    # тут обработали текст
    msg["text"] = filename  # это пример вывода в однострочное поле
    txt.delete('1.0', END)  # тут стираем предыдущее содержимое
    txt.insert(END, '\n'.join(filename))  # это пример вывода в многострочное поле


win = Tk()
win.title("lab-02")
win.geometry("500x400")
font = ("Consolas", 12)

ent = Entry(win, width=72, font=font)
ent.insert(0, "тут будет имя файла")
ent.pack(pady=10)  # это поле для ввода

btn = Button(win, font=font, width=20, text='Solver Task 01', command=set_msg)
btn.pack(pady=10)

msg = Message(win, width=340, font=font, text="тут будет ответ")
msg.pack(anchor=W, pady=10)  # это ОДНОстрочное поле для вывода

txt = Text(wrap="word", width=400, height=300, font=font)
txt.pack(pady=10)  # это МНОГОстрочное поле для вывода

win.mainloop()

