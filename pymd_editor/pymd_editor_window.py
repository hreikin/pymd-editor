from pymd_editor.pymd_editor_frame import EditorFrame

import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class PyMarkdownEditor(ttk.Frame):
    def __init__(self, master=None, **kwargs):
        """
        A Markdown editor with HTML Preview window.
        """
        ttk.Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        """Construct the layout."""
        # Create the editor/preview frame
        self.editor = EditorFrame(self.master)
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

        # Configure the menus.
        self.master.config(menu=self.main_menu)