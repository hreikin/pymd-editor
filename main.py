from editor import editor

# from tkinter import *
import tkinter as tk
from tkinter import font
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
# from ttkbootstrap import Notebook

import logging

##################################### LOGS #####################################
# Initialize the logger and specify the level of logging. This will log "DEBUG" 
# and higher messages to file and log "INFO" and higher messages to the console.
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s: %(message)s',
                    datefmt='%d-%m-%y %H:%M:%S',
                    filename='debug.log',
                    filemode='w')

# Define a "handler" which writes "INFO" messages or higher to the "sys.stderr".
console = logging.StreamHandler()
console.setLevel(logging.INFO)

# Set a format which is simpler for console messages.
formatter = logging.Formatter('[%(asctime)s]: %(message)s', datefmt='%H:%M:%S')

# Tell the console "handler" to use this format.
console.setFormatter(formatter)

# Add the "handler" to the "root logger".
logging.getLogger('').addHandler(console)

################################################################################

class PyMarkdownEditor(ttk.Frame):
    def __init__(self, master=None):
        """Create a subclass of Frame for our window and then initialize and set 
        the variables."""
        ttk.Frame.__init__(self, master)
        self.master = master
        self.myfont = font.Font(family="Ubuntu", size=16)
        self.init_window()

    def init_window(self):
        """Construct the layout."""
        # Create the editor/preview frame
        self.editor = editor.Editor(self.master)
        self.editor.pack(fill="both", expand=1)

        # Create main menu layout.
        self.main_menu = ttk.Menu(self)
        self.file_menu = ttk.Menu(self.main_menu)
        self.file_menu.add_command(label="Open Markdown File", command=self.editor.open_md_file)
        self.file_menu.add_command(label="Save as", command=self.editor.save_as_md_file)
        self.file_menu.add_command(label="Save", command=self.editor.save_md_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.quit)
        self.main_menu.add_cascade(label="File", menu=self.file_menu)

        # Create edit menu layout.
        self.edit_menu = ttk.Menu(self.main_menu)
        self.edit_menu.add_command(label="Copy", command=lambda: self.focus_get().event_generate("<<Copy>>"), accelerator="Ctrl+C")
        self.edit_menu.add_command(label="Cut", command=lambda: self.focus_get().event_generate("<<Cut>>"), accelerator="Ctrl+X")
        self.edit_menu.add_command(label="Paste", command=lambda: self.focus_get().event_generate("<<Paste>>"), accelerator="Ctrl+V")
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Undo", command=lambda: self.focus_get().event_generate("<<Undo>>"), accelerator="Ctrl+Z")
        self.edit_menu.add_command(label="Redo", command=lambda: self.focus_get().event_generate("<<Redo>>"), accelerator="Ctrl+Y")
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Find", command=self.editor.find, accelerator="Ctrl+F")
        self.edit_menu.add_command(label="Select All", command=self.editor.select_all, accelerator="Ctrl+A")
        self.main_menu.add_cascade(label="Edit", menu=self.edit_menu)

        # Create right click menu layout for the editor.
        self.right_click = ttk.Menu(self.editor.text_area)
        self.right_click.add_command(label="Copy", command=lambda: self.focus_get().event_generate("<<Copy>>"), accelerator="Ctrl+C")
        self.right_click.add_command(label="Cut", command=lambda: self.focus_get().event_generate("<<Cut>>"), accelerator="Ctrl+X")
        self.right_click.add_command(label="Paste", command=lambda: self.focus_get().event_generate("<<Paste>>"), accelerator="Ctrl+V")
        self.right_click.add_separator()
        self.right_click.add_command(label="Undo", command=lambda: self.focus_get().event_generate("<<Undo>>"), accelerator="Ctrl+Z")
        self.right_click.add_command(label="Redo", command=lambda: self.focus_get().event_generate("<<Redo>>"), accelerator="Ctrl+Y")
        self.right_click.add_separator()
        self.right_click.add_command(label="Find", command=self.editor.find, accelerator="Ctrl+F")
        self.right_click.add_command(label="Select All", command=self.editor.select_all, accelerator="Ctrl+A")

        # Bind mouse/key events to functions.
        self.editor.text_area.bind_all("<Control-f>", self.editor.find)
        self.editor.text_area.bind_all("<Control-a>", self.editor.select_all)
        self.editor.text_area.bind("<Button-3>", self.popup)

        # Configure the menus.
        self.master.config(menu=self.main_menu)

    def popup(self, event):
        """Right-click popup at mouse location."""
        self.right_click.post(event.x_root, event.y_root)


            
# Instantiate the root window, set the screen size and instantiate the PDF 
# Toolbox window before running the main loop.
if __name__ == "__main__":
    # root = ttk.Tk()
    # style = ttk.Style("darkly")
    # root = ttk.Window()
    root = ttk.Window(themename="darkly")
    root.title("PDF Toolbox")
    screen_height = root.winfo_screenheight()
    screen_width = root.winfo_screenwidth()
    root.geometry(f"{screen_width}x{screen_height}")
    app = PyMarkdownEditor(root)
    app.mainloop()
