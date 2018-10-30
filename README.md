LTSP Killer.py
===============

This is a small python script that I wrote for teaching in LTSP classroms. It prevents users to access specified programs.

* *Example 1*: If I'm teaching something that not requires access to the net I can start this script to avoid pupils to use web related programs for the time of the lesson. 

* *Example 2*: I'm teaching... so no video games are allowed. I tell killer.py to kill all the gnome games.. At the end of the lesson pupils can play.

The basic functioning is simple: every 20 seconds the script checks if any of the target processes is running and brutally kills it.

Usage
-----

* Open a terminal and go to the killer.py folder
* `./killer.py <arguments>`

Arguments accepted are:

* any software executable name (check with top or pgrep for process exact name) *e.g.* `./killer.py firefox-bin gedit` will block Firefox and Gedit
* a predefined group of programs *e.g.* <./killer.py games> will block all the softwares in the *games* group (gcompris, gnomines, same-gnome, ktuberling, gnibbless and some more)

Single user blocking
--------------------

Killer.py can be used to prevent only a certain user to prevent to access the software or group, I added this because of a pupil that wanted to do some programming in the wrong moment. 

* ./killer.py software,user *e.g.* `./killer.py gedit,philip`

Customizing groups
------------------

Groups are defined in the first lines of the killer.py file, just add them properly with any text editor.


Localization
------------
All the few messages are in Italian language.


License
-------
This software is licensed under the *GNU/GPL* license, see [here](http://www.gnu.org/copyleft/gpl.html) for details.
