from Tkinter import *

class AllWidgets():
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
        Label(self.frame, text="Label").pack(side=TOP)
        Button(self.frame, text="Button").pack(side=TOP)
        
        Entry(self.frame, text="Entry").pack(side=TOP)
        lb = Listbox(self.frame, height=3)
        lb.pack(side=TOP)
        for x in ('Listbox 1', 'Listbox 2', 'Listbox 3'):
            lb.insert('end', x)
        #RadioButton(self.frame, text="Radio Button").pack(side=TOP)
        LabelFrame(self.frame, text="Label Frame").pack(side=TOP)
        Scale(self.frame, from_=0, to=200, orient=HORIZONTAL).pack(side=TOP)
        Scrollbar(self.frame, orient=HORIZONTAL).pack(side=TOP, fill=X)
        Spinbox(self.frame, from_=0, to=200).pack(side=TOP)
        p = PhotoImage(file="image.gif")
        l=Label(self.frame, image=p)
        l.image = p
        l.pack(side=TOP)
        
        t = Text(self.frame, height=5, width=20)
        t.pack(side=TOP)
        t.insert(END, "An editable\ntext widget")
        

    def quit(self):
        self.frame.quit()

if __name__ == '__main__':
    root = Tk()
    
    app = AllWidgets(root)
    
    root.mainloop()
