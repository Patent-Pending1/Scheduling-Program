from tkinter import *
from tkinter import ttk

root = Tk()

timeDict = {}
guardDict = {}
parallelList = []

def addGuard(event=None):
    global entry
    guardName,guardStart,guardEnd = entry.get().split()
    tempList = []
    for i in range(2*(int(guardEnd)-int(guardStart))):
        tempList.append((int(guardStart)-10)*2+i)
        parallelList.append((int(guardStart)-10)*2+i)
    guardDict[guardName] = tempList

entry = Entry(root)
entry.pack(padx=10,pady=10)
entry.focus_set()
entry.bind()

def buttonFunc(event=None):
    addGuard()
    entry.delete(0,END)
    entry.focus_set()
def finishFunc(event=None,handler=None):
    root.destroy()

root.bind('<Return>',buttonFunc)
root.bind('<Delete>',finishFunc)

addButton = Button(root,text='ADD GUARD',command=buttonFunc)
addButton.pack()

finishButton = Button(root,text='FINISH',command=finishFunc)
finishButton.pack(side='bottom',padx=10,pady=10)

root.mainloop()

while True:
    try:
        addGuard()
    except:
        break

for i in range(20):
    tempList = []
    for item in guardDict:
        if (guardDict[item]).count(i) == 1:
            tempList.append(item)
    timeDict[str(i)] = tempList

max = 0
for item in parallelList:
    if parallelList.count(item) > max:
        max = parallelList.count(item)

schedule = []
for r in range(20):
    tempList = []
    currentMax = len(timeDict[str(r)])
    for c in range(currentMax):
        try:
            tempList.append((r+c)%currentMax)
        except:
            tempList.append('X')
    schedule.append(tempList)

for r in range(20):
    frontCount = False
    currentMax = len(timeDict[str(r)])
    if currentMax == 5:
        for c in range(currentMax):
            if schedule[r][c] == 0:
                schedule[r][c] = 'indoor'
            elif schedule[r][c] == 1:
                schedule[r][c] = 'main'
            elif schedule[r][c] == 2:
                if c % 3 == 0:
                    schedule[r][c] = 'clean'
                elif frontCount == False:
                    schedule[r][c] = 'front'
                    frontCount == True
                else:
                    schedule[r][c] = 'break'
            elif schedule[r][c] == 3:
                schedule[r][c] = 'hell'
            elif schedule[r][c] == 4:
                schedule[r][c] = 'baby'
    elif currentMax == 6:
        for c in range(currentMax):
            if schedule[r][c] == 0:
                schedule[r][c] = 'indoor'
            elif schedule[r][c] == 1:
                schedule[r][c] = 'main'
            elif schedule[r][c] == 2:
                if c % 3 == 0:
                    schedule[r][c] = 'clean'
                elif frontCount == False:
                    schedule[r][c] = 'front'
                    frontCount == True
                else:
                    schedule[r][c] = 'break'
            elif schedule[r][c] == 3:
                schedule[r][c] = 'hell'
            elif schedule[r][c] == 4:
                schedule[r][c] = 'baby'
            elif schedule[r][c] == 5:
                if c % 3 == 0:
                    schedule[r][c] = 'clean'
                elif frontCount == False:
                    schedule[r][c] = 'front'
                    frontCount == True
                else:
                    schedule[r][c] = 'break'
    elif currentMax == 7:
        for c in range(currentMax):
            if schedule[r][c] == 0:
                schedule[r][c] = 'indoor'
            elif schedule[r][c] == 1:
                schedule[r][c] = 'main'
            elif schedule[r][c] == 2:
                if c % 3 == 0:
                    schedule[r][c] = 'clean'
                elif frontCount == False:
                    schedule[r][c] = 'front'
                    frontCount == True
                else:
                    schedule[r][c] = 'break'
            elif schedule[r][c] == 3:
                schedule[r][c] = 'hell'
            elif schedule[r][c] == 4:
                schedule[r][c] = 'baby'
            elif schedule[r][c] == 5:
                schedule[r][c] = 'roaming'
            elif schedule[r][c] == 6:
                if frontCount == False:
                    schedule[r][c] = 'front'
                    frontCount = True
                else:
                    schedule[r][c] = 'break'
    elif currentMax < 5:
        for c in range(currentMax):
            if schedule[r][c] == 0:
                schedule[r][c] = 'indoor'
            elif schedule[r][c] == 1:
                schedule[r][c] = 'main'
            elif schedule[r][c] == 2:
                schedule[r][c] = 'baby'
            elif schedule[r][c] == 3:
                if frontCount == False:
                    schedule[r][c] = 'front'
                    frontCount = True
                else:
                    schedule[r][c] = 'break'
    elif currentMax > 7:
        for c in range(currentMax):
            if schedule[r][c] == 0:
                schedule[r][c] = 'indoor'
            elif schedule[r][c] == 1:
                schedule[r][c] = 'main'
            elif schedule[r][c] == 2:
                if c % 3 == 0:
                    schedule[r][c] = 'clean'
                elif frontCount == False:
                    schedule[r][c] = 'front'
                    frontCount == True
                else:
                    schedule[r][c] = 'break'
            elif schedule[r][c] == 3:
                schedule[r][c] = 'hell'
            elif schedule[r][c] == 4:
                schedule[r][c] = 'baby'
            elif schedule[r][c] == 5:
                if frontCount == False:
                    schedule[r][c] = 'front'
                    frontCount = True
                else:
                    schedule[r][c] = 'break'
            elif schedule[r][c] == 6:
                schedule[r][c] = 'roaming'
            else:
                if c % 3 == 0:
                    schedule[r][c] = 'clean'
                elif frontCount == False:
                    schedule[r][c] = 'front'
                    frontCount == True
                else:
                    schedule[r][c] = 'break'
def finalTransformation():
    element = ''
    for r in range(20):
        currentMax = len(timeDict[str(r)])
        if r == 0 or timeDict[str(r)] != timeDict[str(r-1)]:
            element = element + '\n'+(' '*6)+'|'
            for item in timeDict[str(r)]:
                element = element+str(item+(' '*(7-len(item)))+'|')
            element = element + '\n' + '\n'
        element = element + str(r//2+10)+':'+str(((r%2))*3)+str(0)+' |'
        for c in range(currentMax):
            for i in range(7):
                try:
                    element = element + str(schedule[r][c][i])
                except:
                    element = element + ' '
            element = element + str('|')
        for i in range(max-currentMax):
            element = element + str('_'*7+'|')
        element = element + '\n'
    return element

scheduleGUI = Tk()
scheduleText = Label(scheduleGUI,text=finalTransformation(),font='Courier',anchor='w',justify='left')
scheduleText.pack()
scheduleGUI.mainloop()