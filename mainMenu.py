import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog 
from tkinter.filedialog import asksaveasfile
from algorithms import *

window_width = 550
window_height = 400
file_contents = ''  # contains the contents of the file we choose

''' 
this function is bound to the Encrypt/Decrypt button. We call the encryption/decryption algo in this
function and insert the result (plain text/cipher text) in the text box 
'''

def selectAlgo(opt, key, textBox, e_or_d):
    global file_contents
    if not e_or_d:
        cc = CaesarCipher(int(key))
        cc.plain_text = file_contents
        cc.encryption()
        textBox.insert(END, cc.cipher_text)
    else:
        cc = CaesarCipher(-1*int(key))
        cc.plain_text = file_contents
        cc.encryption()
        textBox.insert(END, cc.cipher_text)

# This function is bound to the Browse Files button. The uploaded file's contents are stored in file_contents
def openFile():
    file = filedialog.askopenfilename(
        initialdir = 'C:/Users/ASUS/Documents',
        title = 'Select a File',
        filetypes=(('Text Files', '*.txt'),)
    )
    f = open(file, 'r')
    global file_contents
    file_contents = f.read()

def open_text_file(text): 
    # file type
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    # show the open file dialog
    f = filedialog.askopenfile(filetypes=filetypes)
    # read the text file and show its content on the Text
    text.insert('1.0', f.readlines())

def save_file(text):
    my_str1 = text  # read from one text box t1
    fob=filedialog.asksaveasfile(filetypes=[('text file','*.txt')],defaultextension='.txt',mode='w')
    try:
        fob.write(my_str1)
        fob.close()
        t1.delete('1.0',END) # Delete from position 0 till end 
        t1.update()  
        b1.config(text="Saved")
        b1.after(3000, lambda: b1.config(text='Save'))
    except :
        print (" There is an error...")

# This method is called from se.py and it creates the Encrypt/Decrypt window.  
def openWindow(master, screen_width, screen_height, title):
    newWindow = Toplevel(master)
    newWindow.title(title)
    global window_height, window_width
    if title == 'Encrypt':
        e_d_Window(newWindow, 0)
    elif title == "view":
        view_window(newWindow)
    else: 
        e_d_Window(newWindow, 1)

# this function basically deals with all the contents inside the encrypt/decrypt window.
def view_window(window):
    text = tk.Text(window, height=12)
    text.grid(column=0, row=0, sticky='nsew')
    open_button = ttk.Button(window,text='Open a File',command= lambda: open_text_file(text))
    open_button.grid(column=0, row=1, sticky='w', padx=10, pady=10)

def e_d_Window(window, e_or_d):
    global window_height, window_width
    for i in range(9):
        window.rowconfigure(i, weight = 1)

    window.columnconfigure(0, weight = 1)
    window.columnconfigure(1, weight = 3)
    window.columnconfigure(2, weight = 3)
    window.columnconfigure(3, weight = 1)

    # option contains the value of the radiobutton
    option = IntVar()
    option1 = Radiobutton(window, text = 'Caesar Cipher', variable = option, value = 0)

    '''
    this frame and text box is the one under the Caesar cipher radiobutton for taking Caesar cipher's key.
    Note: It's common practice to put text boxes inside their own frames to be able to size them properly.
    I've done the same for all text boxes in this program.
    '''
    ccFrame = Frame(window, borderwidth = 1, relief = 'sunken', height = 50, width = 100)
    ccKey = Text(ccFrame)

    option1.grid(column = 1, row = 2, sticky = W)
    ccFrame.grid(column = 1, row = 3, sticky = NW)
    ccFrame.grid_propagate(False)
    ccKey.grid()

    option2 = Radiobutton(window, text = 'Hill Cipher', variable = option, value = 1)
    option2.grid(column = 1, row = 4, sticky = W)

    # frame and text box for input of hill cipher's key 
    hcFrame = Frame(window, borderwidth = 1, relief = 'sunken', height = 50, width = 100)
    hcKey = Text(hcFrame)

    hcFrame.grid(column = 1, row = 5, sticky = NW)
    hcFrame.grid_propagate(False)
    hcKey.grid()
    
    '''
    frame and text box for the text box on the right side of the window where we display output of
    encryption/decryption algorithm
    '''
    container = Frame(window, borderwidth = 1, relief = 'sunken', height = window_height/1.1, width = window_width/1.5)
    container.grid(column = 2, row = 1, rowspan = 6, pady = 20)
    container.grid_propagate(False)
    rawText = Text(container)
    rawText.grid()

    # Encrypt/Decrypt button at the bottom
    if not e_or_d:
        e_or_dButton = Button(window, text = 'Encrypt', command = lambda: selectAlgo(option.get(), ccKey.get('1.0', END), rawText, 0))
    else:
        e_or_dButton = Button(window, text = 'Decrypt', command = lambda: selectAlgo(option.get(), ccKey.get('1.0', END), rawText, 1))

    e_or_dButton.grid(column = 1, row = 6, sticky = W)

    save = Button(window, text = 'save',command=lambda:save_file(rawText.get('1.0',END)))
    save.grid(column = 1,row = 7,sticky = W)

    # Browse files button
    chooseFile = Button(window, text = 'Browse Files', command = lambda: openFile())
    chooseFile.grid(column = 1, row = 1, sticky = W)

    window.mainloop()
