#!/bin/bash

# absolute path to virtual env py interpreter
PYTHON=/home/ops/repos/toolbox/venv/bin/python 

# absolute path to py script
SCRIPT=/home/ops/repos/toolbox/pi/gpio_package_check.py

# absolute path to log file
LOG=/absolute/path/to/log/file.log

echo -e "\n######STARTUP $(date)######\n" >> $LOG 
$PYTHON $SCRIPT >> $LOG 2>&1