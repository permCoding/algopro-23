from tkinter import * # gives access to tkinter GUI library
 
def hello():
    name = textbox1.get() # gets name from textbox1
    print = "Привет " + name # creates Hello name string 
    textbox2["text"] = print # prints that string in textbox2
 
window = Tk() # opens tkinter window
window.title("Names") # sets title of the window as names
window.geometry("600x600") # dimentions

logo = PhotoImage(file = "./note.png") # displays logo.gif in a label widget
logoimage = Label(image = logo) # this can't be changed while the program is running 
logoimage.place(x = 50, y = 20, width=150, height=150) # position and dimentions
 
textbox1 = Entry(text = "") # creates textbox1 where data is entered 
textbox1.place(x = 145, y = 250, width = 225, height = 25) # position and dimentions
textbox1["bg"] = "white" # white background 
textbox1["fg"] = "black" # black font
 
label1 = Label(text = "Enter a name") # creates label with this text
label1.place(x = 20, y = 250, width = 125, height = 25) # position and dimentions
label1["bg"] = "red" # red background 
label1["fg"] = "blue" # blue font
 
textbox2 = Message(text = print) # creates textbox1 displaying the variable print
textbox2.place(x = 145, y = 300, width = 225, height = 25) # position and dimentions
textbox2["bg"] = "yellow" # white background 
textbox2["fg"] = "black" # black font
textbox2['text'] = ''
 
button1 = Button(text = "Press me", command = hello) # creates button which runs the hello sub-program
button1.place(x = 20, y = 300, width = 125, height = 25) # position and dimentions
button1["bg"] = "blue" # blue background 
button1["fg"] = "red" # red font
 
window.mainloop() # keeps program running 