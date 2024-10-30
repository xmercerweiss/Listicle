# Listicle
### _Copyright Xavier Mercerweiss 2024, Licensed under GPLv3_

## Overview
A quick and dirty Python application used to keep a running to-do list via a `tasks` text file. Designed and tested exlusively for Debian systems.

## Installation
Ensure Python 3 and Tkinter are installed and up-to-date before launching.
```bash
$ sudo apt update && sudo apt upgrade
$ sudo apt-get install python3
$ sudo apt-get install python3-tk
```
While Tkinter is part of Python's standard library, some systems may not have tk properly installed. Running these commands before startup should fix any issues.

## Usage
### Graphical User Interface
The GUI allows you to add and remove tasks.

To open the GUI, simply execute `main.py`:
```bash
$ python3 main.py
```
This should open the following window:

<img src="https://raw.githubusercontent.com/xmercerweiss/Listicle/refs/heads/main/media/gui_preview.png" width=100>

Enter the name of a task into the textbox, then either press enter or click the "+Add Task" button, and the item will be added to your to-do list. Tasks may be removed by simply clicking on them. Tasks cannot be reordered within the GUI, but may have their positions changed by editing the `tasks` text file directly. All data is stored in `tasks` as plaintext and is persistent between application launches. 

## Conclusion
Thank you for reading! I work hard on these projects, and knowing someone cared to examine my work means a lot to me. If you have any questions, feel free to reach out to me at mercerweissx@gmail.com.

Happy coding!
