<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Commits][commit-shield]][commit-url]
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <!-- <a href="https://github.com/hreikin/pymd-editor">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a> -->

<h3 align="center">PyMD Editor</h3>

  <p align="center">
    A standalone and embeddable Python based Markdown editor with HTML preview.
    <br />
    <a href="https://hreikin.github.io/pymd-editor/"><strong>Explore the docs »</strong></a>
    <!-- <br />
    <br />
    <a href="https://github.com/hreikin/pymd-editor">View Demo</a>
    · -->
    <a href="https://pypi.org/project/pymd-editor/">PyPi</a>
    ·
    <a href="https://github.com/hreikin/pymd-editor/issues">Report Bug</a>
    ·
    <a href="https://github.com/hreikin/pymd-editor/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <!-- <li><a href="#prerequisites">Prerequisites</a></li> -->
        <li>
          <a href="#installation">Installation</a>
          <ul>
            <li><a href="#install-with-pip">Install With PIP</a></li>
            <li><a href="#install-from-source">Install From Source</a></li>
          </ul>
        </li>
        <li>
          <a href="#usage">Usage</a>
          <ul>
            <li><a href="#standalone">Standalone</a></li>
            <li><a href="#embedded">Embedded</a></li>
          </ul>
        </li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <!-- <li><a href="#acknowledgments">Acknowledgments</a></li> -->
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

A standalone and embeddable Python based Markdown editor with HTML preview.

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

* [Pygments](https://github.com/pygments/pygments)
* [Python](https://www.python.org/)
* [Python Markdown](https://github.com/Python-Markdown/markdown)
* [tkinter](https://docs.python.org/3/library/tkinter.html)
* [tkinterweb](https://github.com/Andereoo/TkinterWeb)
* [ttkbootstrap](https://github.com/israel-dryer/ttkbootstrap)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started
<!-- ### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ``` -->

### Installation
To get a local copy up and running choose one of the below install instructions and follow the steps provided.

#### Install With PIP

The simplest way to install the PyMD Editor is to use `pip`:

```sh
pip install pymd-editor
```

#### Install From Source

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

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
### Usage

#### Standalone

To start the standalone editor simply run the following:

```sh
python3 -m pymd_editor
```

<p align="right">(<a href="#top">back to top</a>)</p>

#### Embedded

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

<!-- _For more examples, please refer to the [Documentation](https://example.com)_ -->

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

<!-- - [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature -->

See the [open issues](https://github.com/hreikin/pymd-editor/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Github Link: [https://github.com/hreikin/pymd-editor](https://github.com/hreikin/pymd-editor)  
PyPi Link: [https://pypi.org/project/pymd-editor/](https://pypi.org/project/pymd-editor/)  
Documentation: [https://hreikin.github.io/pymd-editor/](https://hreikin.github.io/pymd-editor/)  

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#top">back to top</a>)</p> -->

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/hreikin/pymd-editor.svg?style=for-the-badge
[contributors-url]: https://github.com/hreikin/pymd-editor/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/hreikin/pymd-editor.svg?style=for-the-badge
[forks-url]: https://github.com/hreikin/pymd-editor/network/members
[stars-shield]: https://img.shields.io/github/stars/hreikin/pymd-editor.svg?style=for-the-badge
[stars-url]: https://github.com/hreikin/pymd-editor/stargazers
[issues-shield]: https://img.shields.io/github/issues/hreikin/pymd-editor.svg?style=for-the-badge
[issues-url]: https://github.com/hreikin/pymd-editor/issues
[license-shield]: https://img.shields.io/github/license/hreikin/pymd-editor.svg?style=for-the-badge
[license-url]: https://github.com/hreikin/pymd-editor/blob/master/LICENSE.txt
<!-- [linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555 -->
<!-- [linkedin-url]: https://linkedin.com/in/linkedin_username -->
<!-- [product-screenshot]: images/screenshot.png -->
[commit-shield]: https://img.shields.io/github/commit-activity/m/hreikin/pymd-editor?style=for-the-badge
[commit-url]: https://github.com/hreikin/pymd-editor/graphs/commit-activity