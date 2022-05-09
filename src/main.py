import tkinter
from tkinter import *
import tkinter.messagebox
import nettools

window = tkinter.Tk()

failVar = IntVar()
portsVar = IntVar()

def run():
	addressMin = ipminEntry.get()
	addressMax = ipmaxEntry.get()
	portsTest = portsVar.get()
	if portsTest == 0:
		ports = 0
	else :
		ports = (portsEntry.get()).split()
	showfail = failVar.get()
	nettools.main(addressMin, addressMax, ports, showfail)
	tkinter.messagebox.showinfo("Working IPs", f"{len(nettools.workingip_list)}/{nettools.totalAddress}: {nettools.workingip_list}")

ipminLabel = Label(window, text="IP min")
ipminLabel.pack()
ipminEntry = Entry(window, bd=5)
ipminEntry.pack()

ipmaxLabel = Label(window, text="IP max")
ipmaxLabel.pack()
ipmaxEntry = Entry(window, bd=5)
ipmaxEntry.pack()

portsLabel = Label(window, text="Test ports")
portsLabel.pack()
portsRadio1 = Radiobutton(window, text="True", variable=portsVar, value=1)
portsRadio1.pack()
portsRadio2 = Radiobutton(window, text="False", variable=portsVar, value=0)
portsRadio2.pack()

portsLabel = Label(window, text="Ports")
portsLabel.pack()
portsEntry = Entry(window, bd=5)
portsEntry.pack()

failLabel = Label(window, text="Show fail")
failLabel.pack()
failRadio1 = Radiobutton(window, text="True", variable=failVar, value=1)
failRadio1.pack()
failRadio2 = Radiobutton(window, text="False", variable=failVar, value=0)
failRadio2.pack()

runButton = tkinter.Button(window, text="Run", command=run)
runButton.pack()

window.mainloop()