from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo

win = Tk()
win.title("METANIT.COM")
win.geometry("600x300")
font = 'Consolas 14'
 
def select():
    res = [sel0.get(), sel1.get(), sel2.get()]
    msg = f'cb0={res[0]} cb1={res[1]} cb2={res[2]}'
    # showinfo(title="Info", message=msg)
    result = f"Выбрано: {msg}"
    languages.set(result)
 
position = {"padx":6, "pady":6, "anchor":NW}
 
languages = StringVar()
languages_label = ttk.Label(textvariable=languages)
languages_label.pack(**position)

langs = ['Python', 'JavaScript', 'C#']
sel0 = IntVar()
cb0 = ttk.Checkbutton(text=langs[0], variable=sel0, command=select)
cb0.pack(**position)
 
sel1 = IntVar()
cb1 = ttk.Checkbutton(text=langs[1], variable=sel1, command=select)
cb1.pack(**position)
 
sel2 = IntVar()
cb2 = ttk.Checkbutton(text=langs[2], variable=sel2, command=select)
cb2.pack(**position)
 
win.mainloop()