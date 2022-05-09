import tkinter
from tkinter import *
import nettools

window = tkinter.Tk()

def run():
	addressMin = ipminEntry.get()
	addressMax = ipmaxEntry.get()
	ports = (portsEntry.get()).split()
	status = var.get()
	print(f"{addressMin}, {addressMax}, {ports}, {status}")
	nettools.main(addressMin, addressMax, ports, status)

ipminLabel = Label(window, text="IP min")
ipminLabel.pack()
ipminEntry = Entry(window, bd =5)
ipminEntry.pack()

ipmaxLabel = Label(window, text="IP max")
ipmaxLabel.pack()
ipmaxEntry = Entry(window, bd =5)
ipmaxEntry.pack()

portsLabel = Label(window, text="Ports")
portsLabel.pack()
portsEntry = Entry(window, bd =5)
portsEntry.pack()

var = IntVar()
runLabel = Label(window, text="Show fail")
runLabel.pack()
R1 = Radiobutton(window, text="True", variable=var, value=1)
R1.pack()

R2 = Radiobutton(window, text="False", variable=var, value=0)
R2.pack()

runButton = tkinter.Button(window, text ="Run", command = run)
runButton.pack()

window.mainloop()