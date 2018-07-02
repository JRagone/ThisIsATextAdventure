from tkinter import *

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()
        

        options = dict(sticky=NSEW, padx=0, pady=0)

        self.button = Button(
            frame, text="QUIT", fg="red", command=frame.quit
            )
        self.button.grid(column=0, row=1, **options)

        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.grid(column=0, row=2, **options)

    def say_hi(self):
        print("hi there, everyone!")


if __name__ == '__main__':
    root = Tk()
    root.config(width=100, height=100, bg="black")
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)
    root.resizable(True, False)

    app = App(root)

    root.mainloop()
    root.destroy() # optional; see description below