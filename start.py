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
        text.insert('1.0', 'hello world')
        root.mainloop()

    def __init__(self, root):
        super().__init__(root)
        self.grid_columnconfigure(0, weight=1)

class BlockyCursorText(Text):

    def __init__(self, parent):
        Text.__init__(self, parent, bg='black', fg='green', insertwidth=0,
                      font=font.Font(family='Courier', size=10), highlightthickness=0)

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

        self.after(15, self._place_cursor)

    def _blink_cursor(self):
        '''alternate the background color of the cursorblock tagged text
        every 600 milliseconds'''

        if self.switch == 'green':
            self.switch = 'black'
        else:
            self.switch = 'green'

        self.tag_config('cursorblock', background=self.switch)

        self.after(600, self._blink_cursor)

if __name__ == '__main__':
    Application.main()