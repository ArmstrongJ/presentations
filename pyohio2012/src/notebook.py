from tkinter import *
from tkinter.ttk import *

class TkNotebook():
    def __init__(self, root):
    
        self.frame = Frame(root)
        self.notebook = Notebook(self.frame)
        
        f1 = Frame(self.notebook, width=200, height=100)
        f2 = Frame(self.notebook, width=200, height=100)
        self.notebook.add(f1, text="Page 1")
        self.notebook.add(f2, text="Page 2")
        
        self.label = Label(self.frame, text="A Notebook on the left")
        
        # Layout
        self.frame.grid(row=0, column=0, sticky=(N, S, E, W))
        self.notebook.grid(row=0, column=0, sticky=(N, S, E, W))
        self.label.grid(row=0, column=1, sticky=(E,))
        
        # Resize rules
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=2)
        self.frame.rowconfigure(0, weight=2)
        
    def quit(self):
        self.frame.quit()

if __name__ == '__main__':
    root = Tk()
    
    app = TkNotebook(root)
    
    root.mainloop()