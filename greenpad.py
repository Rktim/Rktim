import tkinter as tk
import os
from tkinter import*
from tkinter.messagebox import *
from tkinter.filedialog import *
 
class Notepad:
 
    rt = Tk()
    W = 507
    H = 678
    TextArea = Text(rt)
    MenuBar = Menu(rt)
    FileMenu = Menu(MenuBar, tearoff=0)
    EditMenu = Menu(MenuBar, tearoff=0)

    ScrollBar = Scrollbar(TextArea)     
    file = None
    
    def __init__(self,**kwargs):

        try:
                self.rt.wm_iconbitmap("Notepad.ico") 
        except:
                pass
 
        try:
            self.W = kwargs['width']
        except KeyError:
            pass
 
        try:
            self.H = kwargs['height']
        except KeyError:
            pass
        self.rt.title("GREENpad")
        
        screenW = self.rt.winfo_screenwidth()
        screenH = self.rt.winfo_screenheight()
        left = (screenW/ 2) - (self.W / 2) 
        top = (screenH / 2) - (self.H /2) 
        self.rt.geometry('%dx%d+%d+%d' % (self.W,self.H,left, top),) 
        self.rt.grid_rowconfigure(0, weight=1)
        self.rt.grid_columnconfigure(0, weight=1)
        
 
        self.TextArea.grid(sticky = N + E + S + W)
         
        self.FileMenu.add_command(label="New",
                                        command=self.__newFile)    

        self.FileMenu.add_command(label="Open",
                                        command=self.openFile)
         
        self.FileMenu.add_command(label="Save",
                                        command=self.__saveFile)        
        self.FileMenu.add_separator()                                         
        self.FileMenu.add_command(label="Exit",
                                        command=self.__quitApplication)
        self.MenuBar.add_cascade(label="File",
                                       menu=self.FileMenu)     
        self.EditMenu.add_command(label="Cut",
                                        command=self.__cut)             
       
        self.EditMenu.add_command(label="Copy",
                                        command=self.__copy)         
      
        self.EditMenu.add_command(label="Paste",
                                        command=self.__paste)         
         
        self.MenuBar.add_cascade(label="Edit",
                                       menu=self.EditMenu)     
         
        self.rt.config(menu=self.MenuBar)
        self.ScrollBar.pack(side=RIGHT,fill=Y)                         
        self.ScrollBar.config(command=self.TextArea.yview)     
        self.TextArea.config(yscrollcommand=self.ScrollBar.set)
     
         
    def __quitApplication(self):
        self.rt.destroy()
        
    def openFile(self):
         
        self.file = askopenfilename(defaultextension=".txt",
                                      filetypes=[("All Files","*.*"),
                                        ("Text Documents","*.txt")])
 
        if self.file == "":
            
            self.file = None
        else:
            self.rt.title(os.path.basename(self.file) + " - Notepad")
            self.TextArea.delete(1.0,END)
 
            file = open(self.file,"r")
 
            self.TextArea.insert(1.0,file.read())
 
            file.close()
 
         
    def __newFile(self):
        self.rt.title("Untitled - Notepad")
        self.file = None
        self.TextArea.delete(1.0,END)
 
    def __saveFile(self):
 
        if self.file == None:
            self.file = asksaveasfilename(initialfile='Untitled.txt',
                                            defaultextension=".txt",
                                            filetypes=[("All Files","*.*"),
                                                ("Text Documents","*.txt")])
 
            if self.file == "":
                self.file = None
            else:
                file = open(self.file,"w")
                file.write(self.TextArea.get(1.0,END))
                file.close()
                self.rt.title(os.path.basename(self.file) + " - Notepad")
                 
             
        else:
            file = open(self.file,"w")
            file.write(self.TextArea.get(1.0,END))
            file.close()
 
    def __cut(self):
        self.TextArea.event_generate("<<Cut>>")
 
    def __copy(self):
        self.TextArea.event_generate("<<Copy>>")
 
    def __paste(self):
        self.TextArea.event_generate("<<Paste>>")
 
    def run(self):
        self.rt.mainloop()
notepad = Notepad(width=600,height=400)
notepad.run()