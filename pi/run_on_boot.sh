#!/bin/bash

#This is an example for a script that runs on boot and logs the output of the referenced script 
#or any errors encountered when running. Add the absolute path to script to crontab file (crontab -e):
#@reboot /home/ops/repos/toolbox/pi/run_on_boot.sh &
#remember to make the script executable with chmod u+x run_on_boot.sh

# absolute path to virtual env py interpreter
PYTHON=/home/ops/repos/toolbox/venv/bin/python 

# absolute path to py script
SCRIPT=/home/ops/repos/toolbox/pi/gpio_pkg_check.py

# absolute path to log file
LOG=/home/ops/repos/toolbox/pi/gpio_pkg_check.log

echo -e "\n######STARTUP $(date)######\n" >> $LOG 
$PYTHON $SCRIPT >> $LOG 2>&1