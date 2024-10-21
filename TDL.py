import tkinter as tk
from tkinter import *

taskList = []
taskDict = {}

def clear():
    taskList = []
    taskDict = {}

def entryWindow():

    entryBox = Tk()
    entryBox.geometry('175x75')

    def inputToList(event=None):
        taskName = nameEntry.get()
        taskPrio = prioEntry.get()
        if taskPrio == None:
            taskPrio = 0
        if taskName not in taskList:
            taskList.append(taskName)
        try:
            taskDict[taskName] = taskPrio
        except:
            pass
        nameEntry.delete(0,END)
        prioEntry.delete(0,END)
        nameEntry.focus_set()

    name = Label(entryBox,text="Task")
    prio = Label(entryBox,text="Prio")
    nameEntry = Entry(entryBox,width=20)
    prioEntry = Entry(entryBox,width=5)
    inputButton = Button(entryBox,text="Enter",command=inputToList)
    quitButton = Button(entryBox,text="Quit",command=entryBox.destroy)

    name.grid(column=0,row=0)
    prio.grid(column=1,row=0)
    nameEntry.grid(column=0,row=1,padx=5)
    prioEntry.grid(column=1,row=1)
    inputButton.grid(column=0,row=2,pady=5)
    quitButton.grid(column=1,row=2,pady=5)

    entryBox.bind('<Return>',inputToList)

    entryBox.mainloop()

root = Tk()
root.geometry('400x200')

clearButton = Button(root,text="clear",command=clear)
addButton = Button(root,text="Add",command=entryWindow)

addButton.grid(column=0,row=len(taskList))
clearButton.grid(column=1,row=len(taskList))

root.mainloop()