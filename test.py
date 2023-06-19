from tkinter import *

def multiplier(*args):
    try:
        value = float(ment.get())
        result.set(value * 2)
    except ValueError:
        pass

mGui = Tk()
mGui.geometry("300x300+300+300")

ment = StringVar()
result = StringVar()

mbutton = Button (mGui, text = "Calculate", command = multiplier)
mbutton.pack()

mEntry = Entry(mGui, textvariable = ment, text="bebe")
mEntry.pack()

mresult = Label(mGui, textvariable = result)
mresult.pack()