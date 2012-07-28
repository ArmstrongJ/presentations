from tkinter import *
from tkinter.ttk import *

class TkCanvas():
    def __init__(self, root):
    
        self.frame = Frame(root)
        self.canvas = Canvas(self.frame)
        self.canvas.grid(row=0, column=0)
        
        self.draw_rect()
        
        quit_button = Button(self.frame, text='Quit', command=self.quit)
        quit_button.grid(row=1, column=0, sticky=(S,E))
        
        self.frame.pack(fill=BOTH, expand=True)
        
    def draw_rect(self):
        self.canvas.create_rectangle((100,100), (30,40))
        
    def quit(self):
        self.frame.quit()

if __name__ == '__main__':
    root = Tk()
    
    app = TkCanvas(root)
    
    root.mainloop()