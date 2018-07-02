import tkinter.ttk
from tkinter.constants import *
from tkinter import *
from tkinter import font

class Application(tkinter.ttk.Frame):

    @classmethod
    def main(cls):
        root = tkinter.Tk()
        app = cls(root)
        app.grid(sticky=NSEW)
        root.grid_columnconfigure(0, weight=1)
        root.grid_rowconfigure(0, weight=1)
        root.resizable(True, False)
        text = BlockyCursorText(root)
        options = dict(sticky=NSEW, padx=0, pady=0)
        text.grid(column=0, row=0, **options)
        text.bind("<Return>", callback)
        text.bind("<Button-1>", lambda e: "break")
        # text.bind("<ButtonRelease-1>", lambda event, arg=text: on_mouse_down(arg))
        adventure = Adventure(text)
        text2 = BlockyCursorText(root)
        text2.grid(column=0, row=1, **options)
        text.focus_set()
        root.mainloop()

    def __init__(self, root):
        super().__init__(root)
        self.grid_columnconfigure(0, weight=1)


def callback(event):
    input = event.widget.get("end-1c linestart", "end-1c")
    with open('gamesave.txt', 'a') as f:
        f.write(input)
    response = "\nYou entered %s" % input
    event.widget.insert(event.widget.index(INSERT), response)

# Called before cursor moves?
def callback2(event):
    print(event.widget.index('insert'))
    # event.widget.after(1000, followup(event.widget))


def on_mouse_down(text):
    print(text.index('insert+1c'))
    print(text.index('end-1c'))
    if text.index('insert+1c') == text.index('end-1c'):
        text.mark_set('insert', text.index('insert-1c'))
    print(text.index('insert+1c'))
    return "break"

class BlockyCursorText(Text):

    def __init__(self, parent):
        Text.__init__(self, parent, bg='black', fg='green', insertwidth=0,
                      font=font.Font(family='Courier', size=20), highlightthickness=0)

        # initialize the cursor position and the color of the cursor
        self.cursor = '1.0'
        self.switch = 'green'

        self._blink_cursor()
        self._place_cursor()
        self.grid_columnconfigure(0, weight=1)


    def _place_cursor(self):
        '''check the position of the cursor against the last known position
        every 15ms and update the cursorblock tag as needed'''

        current_index = self.index('insert')

        if self.cursor != current_index:  # if the insertcursor moved

            self.cursor = current_index   # store the new index
            self.tag_delete('cursorblock')# delete the cursorblock tag

            start = self.index('insert')  # get the start
            end = self.index('insert+1c') # and stop indices

            if start[0] != end[0]:         # this handles an index that
                self.insert(start, ' ')    # reaches the end of the line
                end = self.index('insert') # by inserting a space

            self.tag_add('cursorblock', start, end) # add the tag back in
            self.mark_set('insert', self.cursor)    # move the insertcursor

        if self.index('insert+1c') == self.index('end-1c'):
            self.mark_set('insert', self.index('insert-1c'))

        self.after(15, self._place_cursor)

    def _blink_cursor(self):
        '''alternate the background color of the cursorblock tagged text
        every 600 milliseconds'''

        if self.switch == 'green':
            self.switch = 'black'
        else:
            self.switch = 'green'

        self.tag_config('cursorblock', background=self.switch)

        self.after(800, self._blink_cursor)
        

class Adventure(Text):

    def __init__(self, text_widget):
        self.text_widget = text_widget
        self.name = "Player"
        self.introduce()

    def introduce(self):
        text = "Hello, %s. What is your name?\n\n" % self.name
        self.text_widget.insert('1.0', text)
        self.text_widget.delete(self.text_widget.index(INSERT), 'end')

if __name__ == '__main__':
    Application.main()