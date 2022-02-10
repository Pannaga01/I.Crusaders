
from tkinter import *
from tkinter import ttk
import tkinter as tk

# Top level window
frame = tk.Tk()
frame.title("TextBox Input")
frame.geometry('400x400')

lblChoice = tk.Label(frame, text = "how do you want to encrypt: ").grid(row=0,column=0) 

rb = IntVar()

R1 = Radiobutton(frame, text = "give text", 
                 variable = rb, value = 1,command = lambda : giveText())
R2 = Radiobutton(frame, text = "select a file", 
                 variable = rb, value = 2,command = lambda : ChooseFile())
R1.grid(row=0,column=1)
R2.grid(row=1,column=1)

def ChooseFile():

    lblChooseFile = tk.Label(frame, text = "choose a file: ")
    lblChooseFile.grid(row=5,column=0)

    n = tk.StringVar()
    fileChosen = ttk.Combobox(frame, width = 27, textvariable = n)
  
# Adding combobox drop down list
    fileChosen['values'] = (' January', 
                          ' February',
                          ' March',
                          ' April',
                          ' May',
                          ' June',
                          ' July',
                          ' August',
                          ' September',
                          ' October',
                          ' November',
                          ' December')
  
    fileChosen.grid(column = 1, row = 5)
    fileChosen.current()

def giveText():


    lbl1 = tk.Label(frame, text = "enter you text here: ")
    lbl1.grid(row=2,column=0)

    inputtxt = tk.Text(frame,
                    height = 5,
                    width = 20)
    inputtxt.grid(row=2,column=1)

    # Function for getting Input
    # from textbox and printing it 
    # at label widget
    def printInput():
        inp = inputtxt.get(1.0, "end-1c")
        lbl.config(text = "Provided Input: "+inp)


    
    # Button Creation
    printButton = tk.Button(frame,
                            text = "Print", 
                            command = printInput)
    printButton.grid(row=4)
    
    # Label Creation
    lbl = tk.Label(frame, text = "")
    lbl.grid(row=4)

frame.mainloop()

=======
import tkinter as tk
  
# Top level window
frame = tk.Tk()
frame.title("TextBox Input")
frame.geometry('400x200')
# Function for getting Input
# from textbox and printing it 
# at label widget
  
def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    lbl.config(text = "Provided Input: "+inp)
  

#label fot text box
lbl1 = tk.Label(frame, text = "enter you text here: ")
lbl1.pack()
# TextBox Creation

inputtxt = tk.Text(frame,
                   height = 5,
                   width = 20)
  
inputtxt.pack()
  
# Button Creation
printButton = tk.Button(frame,
                        text = "Print", 
                        command = printInput)
printButton.pack()
  
# Label Creation
lbl = tk.Label(frame, text = "")
lbl.pack()
frame.mainloop()
>>>>>>> 6cb626dbbfb0f0618f927bcf0aa8cbba2fbfee27
