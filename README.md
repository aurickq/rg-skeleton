This is a starter kit for robotgame that hacks together module support. Put source files of bot in src/ and use the makefile to 'compile' the source. This will merge the separate files into one that can be submitted to robotgame.net. The name of the bot can be changed in the makefile and code should be initially written in ai.py.

To change the name of your bot, edit the ROBOTNAME variable in makefile.

To change the python command used, edit the PYTHON variable in makefile.

Since rgcombine will expand your source by as much as 10x by default, you may not be able to submit it to robotgame.net. Running "make release" instead of "make" will compile a short version without useful exception information.
