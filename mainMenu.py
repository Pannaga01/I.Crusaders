from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from algorithms import *

window_width = 550
window_height = 400

cc = CaesarCipher(5)

def openFile(textBox):
    file = filedialog.askopenfilename(
        initialdir = 'C:/Users/ASUS/Documents',
        title = 'Select a File',
        filetypes=(('Text Files', '*.txt'),)
        )
    f = open(file, 'r')
    cc.plain_text = f.read()
    cc.encryption()
    textBox.insert(END, cc.cipher_text)
    
def openWindow(master, screen_width, screen_height, title):
    newWindow = Toplevel(master)
    newWindow.title(title)
    global window_height, window_width
    
    xCoordinate = int(screen_width/2 - window_width/2)
    yCoordinate = int(screen_height/2 - window_height/2)
    newWindow.geometry('{}x{}+{}+{}'.format(window_width, window_height, xCoordinate, yCoordinate)) 
    if title == 'Encrypt': encryptWindow(newWindow)

def giveText(window):

    def printInput():
        inp = inputtxt.get(1.0, "end-1c")
        lbl.config(text = "Provided Input: "+inp)
        #obj = module.user()
        #user.text = inp


    lbl1 = Label(window, text = "enter you text here: ")
    lbl1.grid(row=2,column=0)

    inputtxt = Text(window,
                    height = 5,
                    width = 20)
    inputtxt.grid(row=2,column=1)

    # Function for getting Input
    # from textbox and printing it 
    # at label widge

    # Label Creation
    lbl = Label(window, text = "")
    lbl.grid(row=5)
    # Button Creation
    printButton = Button(window,
                            text = "Print", 
                            command = printInput)
    printButton.grid(row=4)

def chooseFile(window):
    chooseFile = Button(window, text = 'Browse Files', command = lambda: openFile(rawText)).grid(column = 1, row = 2)
    container = Frame(window, borderwidth = 1, relief = 'sunken', width = window_width//1.1, height = window_height//1.1)
    container.grid(column = 1, row = 3)
    container.grid_propagate(False)
    rawText = Text(container)
    rawText.grid()
    chooseFile.bind(lambda: openFile(rawText))

def encryptWindow(window):
    global window_height, window_width
    window.rowconfigure(0, weight = 1)
    window.rowconfigure(1, weight = 1)
    window.rowconfigure(2, weight = 2)
    window.rowconfigure(3, weight = 2)

    window.columnconfigure(0, weight = 1)
    window.columnconfigure(1, weight = 3)
    window.columnconfigure(2, weight = 1)

    lblChoice = Label(window, text = "how do you want to encrypt: ").grid(row=0,column=0) 

    rb = IntVar()

    R1 = Radiobutton(window, text = "give text", 
                    variable = rb, value = 1,command = lambda : giveText(window))
    R2 = Radiobutton(window, text = "select a file", 
                    variable = rb, value = 2,command = lambda : chooseFile(window))
    R1.grid(row=0,column=1)
    R2.grid(row=1,column=1)


    window.mainloop()