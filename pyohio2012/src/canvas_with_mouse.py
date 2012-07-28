from tkinter import *
from tkinter.ttk import *

class TkCanvas():
    def __init__(self, root):
    
        self.frame = Frame(root)
        self.canvas = Canvas(self.frame)
        self.canvas.grid(row=0, column=0, sticky=(N,S,E,W))
        
        self.draw_rect()
        
        quit_button = Button(self.frame, text='Quit', command=self.quit)
        quit_button.grid(row=1, column=0, sticky=(S,E))
        
        self.frame.columnconfigure(0, weight=2)
        self.frame.rowconfigure(0, weight=2)
        
        self.frame.pack(fill=BOTH, expand=True)
        
        self.canvas.bind("<Button-1>", self.start_line)
        self.canvas.bind("<B1-Motion>", self.draw_line)
        self.initial = (0,0)
        
    def start_line(self, event):
        self.initial = (event.x, event.y)
        
    def draw_line(self, event):
        self.canvas.create_line((self.initial[0], self.initial[1], event.x, event.y))
        self.initial = (event.x, event.y)
        
    def draw_rect(self):
        self.canvas.create_rectangle((100,100), (30,40))
        
    def quit(self):
        self.frame.quit()

if __name__ == '__main__':
    root = Tk()
    
    app = TkCanvas(root)
    
    root.mainloop()