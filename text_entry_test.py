from tkinter import *

class takeInput(object):

    def __init__(self,requestMessage):
        self.root = Tk()
        self.string = ''
        self.frame = Frame(self.root)
        self.frame.pack()        
        self.acceptInput(requestMessage)

    def acceptInput(self,requestMessage):
        r = self.frame

        k = Label(r,text=requestMessage)
        k.pack(side='left')
        # self.e = Entry(r,text='Name', bd=2, bg='black', fg='green', insertwidth=10, insertbackground='green',)
        # self.e.pack(side='left')
        # self.e.focus_set()
        self.inputentry = Entry(self.root, bg = "#343833", bd = 5, fg = "#00ff00", width = 60, font='Courier')
        self.inputentry.configure(insertbackground = "#00ff00")
        self.inputentry.configure(highlightthickness = 0)
        self.inputentry.configure(insertwidth = 5)
        self.inputentry.icursor(5)
        self.inputentry.insert(self.inputentry.index(INSERT), "Hello")
        self.position = self.inputentry.index(INSERT)
        print(self.position)
        self.inputentry.icursor(self.inputentry.index(INSERT)-.5)
        print(self.inputentry.index(INSERT))
        self.inputentry.pack()

        b = Button(r,text='okay',command=self.gettext)
        b.pack(side='right')

    def gettext(self):
        self.string = self.inputentry.get()
        self.root.destroy()

    def getString(self):
        return self.string

    def waitForInput(self):
        self.root.mainloop()

def getText(requestMessage):
    msgBox = takeInput(requestMessage)
    #loop until the user makes a decision and the window is destroyed
    msgBox.waitForInput()
    return msgBox.getString()

var = getText('enter your name')
print("Var:", var)