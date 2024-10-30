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

![alt text]()

The _`Subject`_ field designates the name of the activity associated with a given length of time. If left empty, the _`Subject`_ field of the .csv will be listed as `NULL`. Once you've entered the name of an activity, simply hit the "Start" button to begin keeping your time. The amount of time taken _will not_ be listed in the GUI, as I find this simply induces stress in myself. Alt-tab back to whatever you're doing and focus on that; when you're done, come back and hit "Stop."

**NOTE:** Even if you turn off (not sleep, actually shutoff) your computer without hitting "Stop", the program will _still_ log the entry. Ongoing entries are cached and will be retrieved and logged upon next startup, with their _`END`_ time being the moment the shutoff process began.

## Conclusion
Thank you for reading! I work hard on these projects, and knowing someone cared to examine my work means a lot to me. If you have any questions, feel free to reach out to me at mercerweissx@gmail.com.

Happy coding!
