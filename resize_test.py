import tkinter.ttk
from tkinter.constants import *

class Application(tkinter.ttk.Frame):

    @classmethod
    def main(cls):
        tkinter.NoDefaultRoot()
        root = tkinter.Tk()
        app = cls(root)
        app.grid(sticky=NSEW)
        root.grid_columnconfigure(0, weight=1)
        root.grid_rowconfigure(0, weight=1)
        root.resizable(True, False)
        root.mainloop()

    def __init__(self, root):
        super().__init__(root)
        self.create_variables()
        self.create_widgets()
        self.grid_widgets()
        self.grid_columnconfigure(0, weight=1)

    def create_variables(self):
        self.player1 = tkinter.StringVar(self, 'Player 1')
        self.player2 = tkinter.StringVar(self, 'Player 2')
        self.timer = tkinter.StringVar(self)
        self.running = tkinter.BooleanVar(self)

    def create_widgets(self):
        self.set_timer = tkinter.ttk.Entry(self, textvariable=self.timer)
        self.start = tkinter.ttk.Button(self, text='Start', command=self.start)
        self.display1 = tkinter.ttk.Label(self, textvariable=self.player1)
        self.display2 = tkinter.ttk.Label(self, textvariable=self.player2)

    def grid_widgets(self):
        options = dict(sticky=NSEW, padx=3, pady=4)
        self.set_timer.grid(column=0, row=0, **options)
        self.start.grid(column=0, row=1, **options)
        self.display1.grid(column=0, row=2, **options)
        self.display2.grid(column=0, row=3, **options)

    def start(self):
        timer = self.timer.get()
        self.player1.set(timer)
        self.player2.set(timer)

if __name__ == '__main__':
    Application.main()