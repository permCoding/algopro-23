from tkinter import *
from tkinter import ttk
 
win = Tk()
win.title("METANIT.COM")
win.geometry("600x300")
win.grid_columnconfigure(0, weight = 1)
win.grid_rowconfigure(0, weight = 1)

fnt = ('Consolas', 14)

editor = Text(wrap = "word")
editor.grid(column = 0, row = 0, sticky = NSEW)
editor.configure(fg='darkgreen', bg='white', font=fnt)
editor.configure(padx=10, pady=5)

ys = ttk.Scrollbar(orient = "vertical", command = editor.yview)
ys.grid(column = 1, row = 0, sticky = NS)
 
editor["yscrollcommand"] = ys.set

text = open('./text.txt', 'r', encoding='utf8').read()
editor.insert(END, text) 

frame = Frame()
frame.grid(column=0, row=1)
btn1 = Button(frame, text='Go', width=12)
btn1.pack(side=LEFT)
 
btn2 = Button(frame, text='Go', width=12)
btn2.pack(side=LEFT)

win.mainloop()

# from tkinter import *
# from tkinter import ttk


# win = Tk()
# win.title("- Text Widget -")
# win.geometry("720x400+500+200")
# # win.resizable(False, False)
# win.grid_columnconfigure(0, weight=1)
# win.grid_rowconfigure(0, weight=1)


# fnt = ('Consolas', 14)
# txt = Text(win)  # default 80x24 txt['width'] txt['height']
# scrl = Scrollbar(win)

# txt.configure(fg='darkgreen', bg='white', font=fnt)
# txt.configure(wrap=WORD)
# txt.configure(pady=5, padx=15)
# txt.grid(column=0, row=0)

# # ys = ttk.Scrollbar(orient=VERTICAL, command=txt.yview)
# # txt['yscrollcommand']=ys.set


# # ys.pack(side=RIGHT)

# # text = open('./text.txt', 'r', encoding='utf8').read()
# # txt.insert(END, text) 

# win.mainloop()
