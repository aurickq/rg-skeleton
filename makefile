ROBOTNAME=skeleton
PYTHON=python2.7

COMMAND=$(PYTHON) rgcombine.py
TARGET=src/robot.py
OUTPUT=$(ROBOTNAME).py

all:
	$(COMMAND) $(TARGET) $(OUTPUT)
release:
	$(COMMAND) -s $(TARGET) $(OUTPUT)
