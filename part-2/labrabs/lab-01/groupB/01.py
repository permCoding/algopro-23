from tkinter import *


def set_msg():
    # вывести в поле msg через пробел 
    # 5 случайных двузначных целых чисел
    msg['text'] = ent.get()  # string


win = Tk()
win.title("labrab-1")
win.configure(bg="#FFFACD")
win.geometry("666x400+300+100")
win.resizable(False, False)
font = ("Consolas", 16)  # "Consolas 14 Bold"


ent = Entry(win, font=font, width=24)
ent.pack(pady=10)

btn = Button(win, font=font, text="Сгенерировать",
        fg="black", bg="#20B2AA", width=22, command=set_msg)
btn.pack(pady=10)

msg = Message(win, font=font, width=400, 
        bg="#FFFACD", text="- - - - - - - -")
msg.pack(pady=10)

win.mainloop()
