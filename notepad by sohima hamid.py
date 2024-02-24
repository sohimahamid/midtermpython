import tkinter 
import os 
from tkinter import * 
from tkinter.messagebox import * 
from tkinter.filedialog import *
from tkinter.simpledialog import *
from tkinter.font import *
from tkinter.colorchooser import *
 
class Notepad1:
    __root1 = Tk() 
 
    # default Notepad window width and height 
    __thisWidth = 300 
    __thisHeight = 300 
    __thisTextArea = Text(__root1) 
    __thisMenuBar = Menu(__root1) 
    __thisFileMenu = Menu(__thisMenuBar, tearoff=0) 
    __thisEditMenu = Menu(__thisMenuBar, tearoff=0)
    __thisAlignmentMenu = Menu(__thisMenuBar, tearoff=0)
    __thisFormatMenu = Menu(__thisMenuBar, tearoff=0)
    __thisHelpMenu = Menu(__thisMenuBar, tearoff=0)
 
    # To add scrollbar in Notepad 
    __thisScrollBar = Scrollbar(__thisTextArea) 
    __file = None 
 
    def __init__(self, **note): 
 
        # Set icon 
        try: 
            self.__root1.wm_iconbitmap("Notepad.ico") 
        except: 
            pass 
 
        # Set Notepad window size the default is 300x300 
 
        try: 
            self.__thisWidth = note['width'] 
        except KeyError: 
            pass 
 
        try: 
            self.__thisHeight = note['height'] 
        except KeyError: 
            pass 
 
        # Set the Notepad window text 
        self.__root1.title("Untitled - Notepad") 
 
        # Center of the window 
        screenWidth = self.__root1.winfo_screenwidth() 
        screenHeight = self.__root1.winfo_screenheight() 
 
        # For left alling 
        leftallign = (screenWidth / 2) - (self.__thisWidth / 2) 
 
        # For right-allign 
        topallign = (screenHeight / 2) - (self.__thisHeight / 2) 
 
        # For top and bottom 
        self.__root1.geometry('%dx%d+%d+%d' % (self.__thisWidth, 
                                              self.__thisHeight, 
                                              leftallign, topallign)) 
 
        # for making the textarea auto resizable 
        self.__root1.grid_rowconfigure(0, weight=1) 
        self.__root1.grid_columnconfigure(0, weight=1) 
 
        # Add the controls (widget) 
        self.__thisTextArea.grid(sticky=N + E + S + W) 
 
        # for open new file in Notepad 
        self.__thisFileMenu.add_command(label="New", 
                                        command=self.__newFile) 
 
        # for open a already existing file 
        self.__thisFileMenu.add_command(label="Open", 
                                        command=self.__openFile) 
 
        # To save current file of Notepad 
        self.__thisFileMenu.add_command(label="Save", 
                                        command=self.__saveFile)
        
        # To change the background color
        self.__thisFileMenu.add_command(label="Change Background Color",
                                    command=self.__changeBackgroundColor)
 
        # To create a line in the dialog 
        self.__thisFileMenu.add_separator() 
        self.__thisFileMenu.add_command(label="Exit", 
                                        command=self.__quitApplication)
        
        self.__thisMenuBar.add_cascade(label="File", 
                                       menu=self.__thisFileMenu) 
 
        # To give a feature of cut 
        self.__thisEditMenu.add_command(label="Cut", 
                                        command=self.__cut) 
 
        # to give a feature of copy 
        self.__thisEditMenu.add_command(label="Copy", 
                                        command=self.__copy) 
 
        # To give a feature of paste 
        self.__thisEditMenu.add_command(label="Paste", 
                                        command=self.__paste)
        # To give a feature of replace
        self.__thisEditMenu.add_command(label="Replace", 
                                command=self.__replaceText)

        # To give a feature of selectall 
        self.__thisEditMenu.add_command(label="Selectall", 
                                        command=self.__selectall)

        # To give a feature of bold 
        self.__thisEditMenu.add_command(label="Bold", 
                                        command=self.__bold)

        # To give a feature of italic 
        self.__thisEditMenu.add_command(label="Italic", 
                                        command=self.__italic)

        # To give a feature of underline 
        self.__thisEditMenu.add_command(label="underline", 
                                        command=self.__underline) 
 
        # To give a feature of editing 
        self.__thisMenuBar.add_cascade(label="Edit", 
                                       menu=self.__thisEditMenu)
        
        # Add font size option to the Format menu
        self.__thisFormatMenu.add_command(label="Font Size",
                                          command=self.__changeFontSize)

        # Add font color option to the Format menu
        self.__thisFormatMenu.add_command(label="Font Color",
                                          command=self.__changeFontColor)

        #Add font style option to the Format menu
        self.__thisFormatMenu.add_command(label="Font Style",
                                            command=self.__changeFontStyle)

        # Add alignment options to the Alignment menu
        self.__thisAlignmentMenu.add_command(label="Align Left",
                                  command=self.__alignLeft)
        self.__thisAlignmentMenu.add_command(label="Align Center",
                                  command=self.__alignCenter)
        self.__thisAlignmentMenu.add_command(label="Align Right",
                                  command=self.__alignRight)

        # To give a feature of alignment 
        self.__thisMenuBar.add_cascade(label="Alignment", 
                                       menu=self.__thisAlignmentMenu)

        # Add the Format menu to the main menu bar
        self.__thisMenuBar.add_cascade(label="Format", menu=self.__thisFormatMenu)
 
        # for creating the feature of description of the notepad 
        self.__thisHelpMenu.add_command(label="About Notepad", 
                                        command=self.__showAbout) 
        self.__thisMenuBar.add_cascade(label="Help", 
                                       menu=self.__thisHelpMenu) 
 
        self.__root1.config(menu=self.__thisMenuBar) 
 
        self.__thisScrollBar.pack(side=RIGHT, fill=Y) 
 
        # Scrollbar will adjust automatically according to the content 
        self.__thisScrollBar.config(command=self.__thisTextArea.yview) 
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set) 
 
    def __quitApplication(self): 
        self.__root1.destroy() 
 
    # exit() 
 
    def __showAbout(self): 
        showinfo("Notepad", "This Notepad is created by using python") 
 
    def __openFile(self): 
 
        self.__file = askopenfilename(defaultextension=".txt", 
                                      filetypes=[("All Files", "*.*"), 
                                                 ("Text Documents", "*.txt")]) 
 
        if self.__file == "": 
 
            # no file to open 
            self.__file = None 
        else: 
 
            # Try to open the file 
            # set the window title 
            self.__root1.title(os.path.basename(self.__file) + " - Notepad") 
            self.__thisTextArea.delete(1.0, END) 
 
            file = open(self.__file, "r") 
 
            self.__thisTextArea.insert(1.0, file.read()) 
 
            file.close() 
 
    def __newFile(self): 
        self.__root1.title("Untitled - Notepad") 
        self.__file = None 
        self.__thisTextArea.delete(1.0, END) 

    def __changeBackgroundColor(self):
        color = askcolor()
        if color[1]:
                self.__thisTextArea.config(bg=color[1])
 
    def __saveFile(self): 
 
        if self.__file == None: 
            # Save as new file 
            self.__file = asksaveasfilename(initialfile='Untitled.txt', 
                                            defaultextension=".txt", 
                                            filetypes=[("All Files", "*.*"), 
                                                       ("Text Documents", "*.txt")]) 
 
            if self.__file == "": 
                self.__file = None 
            else: 
 
                # Try to save the file 
                file = open(self.__file, "w") 
                file.write(self.__thisTextArea.get(1.0, END)) 
                file.close() 
 
                # for Change the window title 
                self.__root.title(os.path.basename(self.__file) + " - Notepad") 
 
 
        else: 
            file = open(self.__file, "w") 
            file.write(self.__thisTextArea.get(1.0, END)) 
            file.close() 
 
    def __cut(self): 
        self.__thisTextArea.event_generate("<<Cut>>") 
 
    def __copy(self): 
        self.__thisTextArea.event_generate("<<Copy>>") 
 
    def __paste(self): 
        self.__thisTextArea.event_generate("<<Paste>>")

    def __replaceText(self):
        replace_text = askstring("Replace", "Enter text:")
        if replace_text:
            replace_with = askstring("Replace", f"Enter'{replace_text}' with:")
        if replace_with:
            content = self.__thisTextArea.get(1.0, END)
            new_content = content.replace(replace_text, replace_with)
            self.__thisTextArea.delete(1.0, END)
            self.__thisTextArea.insert(1.0, new_content)

    def __selectall(self): 
        self.__thisTextArea.tag_add("sel", '1.0', 'end')

    def __bold(self): 
        self.__thisTextArea.tag_add('bold','sel.first','sel.last')
        self.__thisTextArea.tag_config('bold', font=('Calibri', 18, 'bold'))
        
    def __italic(self):
        self.__thisTextArea.tag_add('italic','sel.first','sel.last')
        self.__thisTextArea.tag_config('italic', font=('Arial', 12, 'italic'))

    def __underline(self): 
        self.__thisTextArea.tag_add('underline','sel.first','sel.last')
        self.__thisTextArea.tag_config('underline', underline=True)

    def __alignLeft(self):
        sel_start, sel_end = self.__thisTextArea.index("sel.first"), self.__thisTextArea.index("sel.last")
        if sel_start and sel_end:
            if sel_end != self.__thisTextArea.index("end"):
                self.__thisTextArea.tag_configure("alignment_left", justify=LEFT)
                self.__thisTextArea.tag_add("alignment_left", sel_start, sel_end)

    def __alignCenter(self):
        sel_start, sel_end = self.__thisTextArea.index("sel.first"), self.__thisTextArea.index("sel.last")
        if sel_start and sel_end:
            if sel_end != self.__thisTextArea.index("end"):
                self.__thisTextArea.tag_configure("alignment_center", justify=CENTER)
                self.__thisTextArea.tag_add("alignment_center", sel_start, sel_end)

    def __alignRight(self):
        sel_start, sel_end = self.__thisTextArea.index("sel.first"), self.__thisTextArea.index("sel.last")
        if sel_start and sel_end:
            if sel_end != self.__thisTextArea.index("end"):
                self.__thisTextArea.tag_configure("alignment_right", justify=RIGHT)
                self.__thisTextArea.tag_add("alignment_right", sel_start, sel_end)

            
    def __changeFontSize(self):
        font_size = askinteger("Font Size", "Enter Font Size:")
        if font_size:
            sel_start, sel_end = self.__thisTextArea.index("sel.first"), self.__thisTextArea.index("sel.last")
            self.__thisTextArea.tag_add("font_size", sel_start, sel_end)
            self.__thisTextArea.tag_config("font_size", font=(None, font_size))

    def __changeFontColor(self):
        color = askcolor()
        if color[1]:
            sel_start, sel_end = self.__thisTextArea.index("sel.first"), self.__thisTextArea.index("sel.last")
            self.__thisTextArea.tag_add("font_color", sel_start, sel_end)
            self.__thisTextArea.tag_config("font_color", foreground=color[1])
            
    def __changeFontStyle(self):
        font_style = askstring("Font Style", "Enter Font Style (e.g. Arial, Algerian, Calibri, Arial Black, Times New Roman):")
        if font_style:
            sel_start, sel_end = self.__thisTextArea.index("sel.first"), self.__thisTextArea.index("sel.last")
            self.__thisTextArea.tag_add("font_style", sel_start, sel_end)
            self.__thisTextArea.tag_config("font_style", font=(font_style,))
        
    def run(self):
 
        # Run main application
        self.__root1.mainloop() 
 
    # Run main application 
 
 
notepad1 = Notepad1(width=600, height=400) 
notepad1.run() 
