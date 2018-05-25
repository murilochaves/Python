from tkinter import *

class App:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.btquit = Button(frame, text='Quit', fg='red', command=self.quit)
        self.btquit.pack(side=LEFT)

        self.bthello = Button(frame, text='Hello', command=self.hello)
        self.bthello.pack(side=LEFT)

    def quit(self):
        root.destroy()

    def hello(self):
        print('Hello world!')

root = Tk()

app = App(root)

root.mainloop()