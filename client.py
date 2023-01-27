from tkinter import *
from tkinter import ttk
import serial


def toggle():
    global console

    console.write("toggle\r\n".encode())


console = serial.Serial("/dev/ttyACM0", baudrate=9600, timeout=1)
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Button(frm, text="Toggle", command=toggle).grid(column=1, row=0)
root.mainloop()
