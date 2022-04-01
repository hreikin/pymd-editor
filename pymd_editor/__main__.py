from pymd_editor.pymd_editor_window import PyMarkdownEditor

import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Instantiate the root window, set the screen size, theme and title and then 
# instantiate the PyMarkdownEditor window before running the main loop.
def main():    
    root = ttk.Window(themename="darkly")
    root.title("Py Markdown Editor")
    screen_height = root.winfo_screenheight()
    screen_width = root.winfo_screenwidth()
    root.geometry(f"{screen_width}x{screen_height}")
    app = PyMarkdownEditor(root)
    app.mainloop()


if __name__ == "__main__":
    main()