from tkinter import *
from random import randint

def do():
    cnt = ent2.get()
    filename = ent1.get()
    f = open(filename, 'w')
    r = [str(randint(100, 999)) for _ in range(int(cnt))]
    f.write(f"{' '.join(r)}\n")
    f.close()

win = Tk()

# imgicon = PhotoImage(file='./display.png')
# win.tk.call('wm', 'iconphoto', win._w, imgicon) 
# win.tk.call('wm', 'iconphoto', win._w, PhotoImage(file='./display.png'))
# win.wm_iconbitmap('green.ico')

img = PhotoImage(file='./display.png')
win.tk.call('wm', 'iconphoto', win._w, img)

win.title("METANIT.COM")
win.geometry("600x300")
font = ('Consolas', 14)

frame1 = Frame(win, width=200)
frame1.pack(pady=20)

lbl1 = Label(frame1, font=font, width=16, text='Имя файла:', fg='grey')
lbl1.pack(side=LEFT)

ent1 = Entry(frame1, font=font, width=16)
ent1.pack(side=LEFT, padx=10)

frame2 = Frame(win, width=200)
frame2.pack(pady=20)

lbl2 = Label(frame2, font=font, width=16, text='Кол-во чисел:', fg='grey')
lbl2.pack(side=LEFT)

ent2 = Entry(frame2, font=font, width=16)
ent2.pack(side=LEFT, padx=10)

btn = Button(win, font=font, width=20, text='Save to file', bg='#4499dd', command=do)
btn.pack()
 
win.mainloop()
