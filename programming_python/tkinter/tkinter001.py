import tkinter
import tkinter.messagebox


tkinter.Label(text='Spam').pack()
tkinter.mainloop()

def reply():
    tkinter.messagebox.showinfo(title='popup', message='Button pressed!')

window = tkinter.Tk()
button = tkinter.Button(window, text='press', command=reply)
button.pack()
window.mainloop()
