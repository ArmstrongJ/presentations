from tkinter import *
from tkinter.ttk import *

class TkTrees():
    def __init__(self, root):
        self.root = root
        
        self.notebook = Notebook(root)
        
        f1 = Frame(self.notebook)
        f2 = Frame(self.notebook)
        self.notebook.add(f1, text="Columned List")
        self.notebook.add(f2, text="Tree")
        
        self.column_treeview(f1)
        self.tree_treeview(f2)

        # Layout
        self.notebook.grid(row=0, column=0, sticky=(N, S, E, W))
        
        # Resize rules
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        
    def column_treeview(self, parent):
    
        columns = ('Name', 'Description')
                   
        self.ctree = Treeview(parent, columns=columns, show="headings")
        for col in columns:
            self.ctree.column(col, width=90)
            self.ctree.heading(col, text=col)

        self.ctree.insert('', 'end', values=('Example', 'One row...'))
        self.ctree.insert('', 'end', values=('Example Part 2', 'Another row...'))

        self.ctree.pack(fill=BOTH, expand=1)
        
    def tree_treeview(self, parent):
                   
        self.ttree = Treeview(parent)

        id = self.ttree.insert('', 'end', text='Example')
        self.ttree.insert(id, 'end', text='First sub item')
        
        id = self.ttree.insert('', 'end', text='Example Part 2')
        self.ttree.insert(id, 'end', text='A different sub item')
        
        self.ttree.pack(fill=BOTH, expand=1)
        
        
    def quit(self):
        self.root.quit()

if __name__ == '__main__':
    root = Tk()
    
    app = TkTrees(root)
    
    root.mainloop()