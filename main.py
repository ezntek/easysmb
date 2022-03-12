from tkinter import *
from tkinter import ttk
import sys

from pygame import GL_CONTEXT_ROBUST_ACCESS_FLAG

def killWindow():
    sys.exit(0)

def connectSrv():
    print("it does not do anything at the moment")

def main():
    root = Tk()
    root.title("easySMB Client")
    root.geometry("500x400")

    window = ttk.Frame(root, padding="12 12 12 12")
    window.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    serverNameLabel = ttk.Label(window, width=10, text="Server Name")
    serverNameLabel.grid(column=0, row=1, sticky=(W, E, N, S))

    srvname = StringVar()
    serverNameEntry = ttk.Entry(window, width=25, textvariable=srvname)
    serverNameEntry.grid(column=1, row=1, sticky=(N,W,E,S)) 

    shareNameLabel = ttk.Label(window, width=40,text="Share Name (leave blank for user volume)")
    shareNameLabel.grid(column=0, row=2, sticky=(N,W,E,S))

    sharename = StringVar()
    shareNameEntry = ttk.Entry(window, width=25, textvariable=sharename)
    shareNameEntry.grid(column=1, row=2, sticky=(N,W,E,S))

    usernameLabel = ttk.Label(window, width=10, text="Username")
    usernameLabel.grid(column=0, row=3, sticky=(W, E, N, S))

    username = StringVar()
    usernameEntry = ttk.Entry(window, width=25, textvariable=username)
    usernameEntry.grid(column=1, row=3, sticky=(N,W,E,S)) 

    passwordLabel = ttk.Label(window, width=10,text="Password")
    passwordLabel.grid(column=0, row=4, sticky=(N,W,E,S))

    password = StringVar()
    passwordEntry = ttk.Entry(window, width=25, textvariable=password, show="*")
    passwordEntry.grid(column=1, row=4, sticky=(N,W,E,S))

    passwordLabel = ttk.Label(window, width=10,text="Password")
    passwordLabel.grid(column=0, row=4, sticky=(N,W,E,S))

    password = StringVar()
    passwordEntry = ttk.Entry(window, width=25, textvariable=password, show="*")
    passwordEntry.grid(column=1, row=4, sticky=(N,W,E,S))
    
    goButton = ttk.Button(window, width=10, command=connectSrv)
    goButton.grid(column=1, row=6, sticky=(N,W,E,S))

    exitButton = ttk.Button(window, width=10, text="Quit", command=killWindow)
    exitButton.grid(column=1, row= 7, sticky=(N,W,E,S))

    root.mainloop()

if  (__name__ == "__main__") :
    main()