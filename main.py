from tkinter import *
from random import randint
import os

window = Tk()


window.geometry("1000x450")

window.resizable(False, False)

window.title("Password Generator")


window['bg'] = '#25333D'


str = "Random Password Generator"
cen = str.center(40)

label = Label(window, text=cen, font=("Arial Bold", 30), bg ="#25333D")


label.pack()




def newRand () :
    passEntry.delete(0, END)
    passLength = int(myEntry.get())
    myPass = ''
    for i in range(passLength) :
        myPass += chr(randint(33, 126))


    passEntry.insert(0, myPass)

def clipper () :
    window.clipboard_clear()
    window.clipboard_append(passEntry.get())


labFrame = LabelFrame(window, text="How many characters?", bg = '#25333D', bd=0, font=("Arial Bold", 15))  # label frame
labFrame.pack(pady=20)

myEntry = Entry(labFrame, font=("Arial Bold", 20))

myEntry.pack(pady=20, padx=20)

passEntry = Entry(window, text='', font=("Arial Bold", 20), bd=0, bg='#25333D')
passEntry.pack(pady = 20)

myFrame = Frame(window, bg = '#25333D')
myFrame.pack(pady = 20)

myButton = Button(myFrame, text="Generate Password", command = newRand, font = "Arial", fg = '#FFFFFF', bg = '#25333D')

myButton.grid(row=0, column=0, padx=10)

clipButton = Button(myFrame, text="Copy to clipboard", command = clipper, font = "Arial", fg = '#FFFFFF', bg = '#25333D')
clipButton.grid(row=0, column=1, padx = 10)


window.mainloop()
