from tkinter import *
from tkinter.tkinter102 import MyGui

mainwin = Tk()
print(f'{mainwin=}')

Label(mainwin, text=__name__).pack()

popup = Toplevel()
print(f'{popup=}')

Label(popup, text='Attach').pack(side=LEFT)
MyGui(popup).pack(side=RIGHT)
mainwin.mainloop()