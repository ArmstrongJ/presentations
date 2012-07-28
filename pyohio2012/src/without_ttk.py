from Tkinter import *

class WithoutTtk():
    def __init__(self, root):
    
        self.frame = Frame(root)
        
        self.build_window()
        
        self.frame.pack(fill=BOTH)
        
        menubar = Menu(root)
        root['menu'] = menubar
        
        menu_file = Menu(menubar)
        menu_file.add_command(label="Quit", command=self.quit)
        
        menubar.add_cascade(menu=menu_file, label='File')
        
        
    def build_window(self):
        label = Label(self.frame, text="How do I look?")
        label.pack(side=TOP)
        
        button_bad = Button(self.frame, text="Terrible", command=self.quit)
        button_bad.pack(side=LEFT)
        
        button_good = Button(self.frame, text="Not too shabby", command=self.quit)
        button_good.pack(side=RIGHT)

    def quit(self):
        self.frame.quit()

if __name__ == '__main__':
    root = Tk()
    
    app = WithoutTtk(root)
    
    root.mainloop()
