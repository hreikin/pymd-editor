<!-- GETTING STARTED -->
# Getting Started
<!-- ### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ``` -->
## Installation
To get a local copy up and running choose one of the below install instructions and follow the steps provided.

### Install With PIP

The simplest way to install the PyMD Editor is to use `pip`:

```sh
pip install pymd-editor
```

### Install From Source

Alternatively you can install from source by following the steps below:

1. Clone the repo:
   ```sh
   git clone https://github.com/hreikin/pymd-editor.git
   cd pymd-editor/
   ```
2. Create and source a Python virtual environment:
   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install requirements with `pip`:
   ```sh
   pip install -r requirements.txt
   ```

<!-- USAGE EXAMPLES -->
## Usage

### Standalone

To start the standalone editor simply run the following:

```sh
python3 -m pymd_editor
```

### Embedded

To use the `ttkbootstrap` styled `EditorFrame` in one of your own python scripts:

```python
from pymd_editor.pymd_editor_frame import EditorFrame

import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window(themename="darkly")
app = EditorFrame(root)
app.pack(fill="both", expand=1)
app.mainloop()
```