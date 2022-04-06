import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="pymd-editor",
    version="0.0.4",
    description="A Python based Markdown editor with HTML preview",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/hreikin/pymd-editor",
    author="hreikin",
    author_email="hreikin@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["pymd_editor"],
    include_package_data=True,
    install_requires=["markdown", "pygments", "tkinterweb", "ttkbootstrap"],
    entry_points={
        "console_scripts": [
            "pymd-editor=pymd_editor.__main__:main",
        ]
    },
)