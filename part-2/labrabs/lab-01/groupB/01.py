from tkinter import *


def set_msg():
    # вывести в поле msg через пробел 
    # 5 случайных двузначных целых чисел
    msg['text'] = str(123)


win = Tk()
win.title("labrab-1")
win.configure(bg="#FFFACD")
win.geometry("666x400+300+100")
font = ("Consolas", 16)  # "Consolas 14 Bold"

btn = Button(win, font=font, text="Сгенерировать",
        fg="black", bg="#20B2AA", command=set_msg)
btn.pack(pady=10)

msg = Message(win, font=font, width=400, 
        bg="#FFFACD", text="- - - - - - - -")
msg.pack(pady=10)




win.mainloop()
