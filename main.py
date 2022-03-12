from tkinter import *
from tkinter import ttk

def main():
    root = Tk()
    root.title("easySMB Client")

    window = ttk.Frame(root, padding="12 12 12 12")
    window.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    serverNameLabel = ttk.Label(window, width=10, text="Server Name")
    serverNameLabel.grid(column=0, row=1, sticky=(W, E, N, S))

    srvname = StringVar()
    serverNameEntry = ttk.Entry(window, width=25, textvariable=srvname)
    serverNameEntry.grid(column=1, row=1, sticky=(N,W,E,S))

    

    root.mainloop()    

if  (__name__ == "__main__") :
    main()