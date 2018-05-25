from tkinter import *

class MouseLocation(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Mouse and Keyboard events')
        self.master.geometry('300x300')

        self.mousePosition = StringVar()
        self.mousePosition.set('Mouse outsite window')
        self.positionLabel = Label(self, textvariable=self.mousePosition)
        self.positionLabel.pack(side=BOTTOM)

        self.bind('<Button-1>', self.buttonLeftClick)
        self.bind('<ButtonRelease-1>', self.buttonLeftRelease)
        self.bind('<Button-2>', self.buttonRightClick)
        self.bind('<ButtonRelease-2>', self.buttonRigthRelease)
        self.bind('<Button-3>', self.buttonCenterClick)
        self.bind('<ButtonRelease-3>', self.buttonCenterRelease)
        self.bind('<Enter>', self.enterWindow)
        self.bind('<Leave>', self.exitWindow)
        self.bind('<B1-Motion>', self.mouseDragged)

        #self.master.bind('<KeyPress>', self.keyPressed)
        #self.master.bind('<KeyRelease>', self.keyReleased)

        self.master.bind('<Control-KeyPress-Tab>', self.comboPressed)

    def buttonLeftClick(self, event):
        self.mousePosition.set('LEFT BUTTON PRESSED AT [' + str(event.x) + ',' + str(event.y) + ']')

    def buttonLeftRelease(self, event):
        self.mousePosition.set('LEFT BUTTON RLEASE AT [' + str(event.x) + ',' + str(event.y) + ']')

    def buttonRightClick(self, event):
        self.mousePosition.set('RIGHT BUTTON PRESSED AT [' + str(event.x) + ',' + str(event.y) + ']')

    def buttonRigthRelease(self, event):
        self.mousePosition.set('RIGHT BUTTON RELEASE AT [' + str(event.x) + ',' + str(event.y) + ']')

    def buttonCenterClick(self, event):
        self.mousePosition.set('CENTER BUTTON PRESSED AT [' + str(event.x) + ',' + str(event.y) + ']')

    def buttonCenterRelease(self, event):
        self.mousePosition.set('CENTER BUTTON RELEASE AT [' + str(event.x) + ',' + str(event.y) + ']')

    def enterWindow(self, event):
        self.mousePosition.set('Mouse in Window')

    def exitWindow(self, event):
        self.mousePosition.set('Mouse outside Window')

    def mouseDragged(self, event):
        self.mousePosition.set('Draggad AT [' + str(event.x) + ',' + str(event.y) + ']')

    def keyPressed(self, event):
        messagebox.showinfo('Key Pressed', 'Any Key Pressed')

    def keyReleased(self, event):
        messagebox.showinfo('Key Released', 'Any Key Release')

    def comboPressed(self, event):
        messagebox.showinfo('Keys Pressed', 'CTRL + SHIFT + TAB')
        

def main():
    MouseLocation().mainloop()

if __name__ == '__main__':
    main()