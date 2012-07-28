try:
    from Tkinter import *
    from ttk import *
except ImportError:
    from tkinter import *
    from tkinter.ttk import *

class TtkWidgets():
    def __init__(self, root):
    
        self.frame = Frame(root)
        
        self.build_window()
        
        self.frame.pack()
        
        menubar = Menu(root)
        root['menu'] = menubar
        
        menu_file = Menu(menubar)
        menu_file.add_command(label="Quit", command=self.quit)
        
        menubar.add_cascade(menu=menu_file, label='File')
        
    def build_window(self):
        cbv = StringVar()
        Combobox(self.frame, textvariable=cbv, 
            values=('Canada', 'Sweden', 'Germany')).pack(side=TOP)

        Checkbutton(self.frame, text='Check').pack(side=TOP)
        Radiobutton(self.frame, text='Radio').pack(side=TOP)
        pb = Progressbar(self.frame, orient=HORIZONTAL, length=200, mode='indeterminate')
        pb.start()

    def quit(self):
        self.frame.quit()

if __name__ == '__main__':
    root = Tk()
    
    app = TtkWidgets(root)
    
    root.mainloop()
