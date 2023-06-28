#!/bin/bash
start="$(date +%s)"
echo "Started logging focus"
read -p "Press Enter to stop recording focus"
echo "Stopped recording focus"
echo "Calculating focus time"
end="$(date +%s)"
logfile="//home/tawishi/Desktop/t./self_track/logs/focus.txt"
if [ -e "$logfile" ];
then
    echo "File exists. Using existing file: $logfile"
else
    # Create the file if it does not exist
    touch "$logfile"
    echo "File created: $logfile"
fi
echo "Start Time: $start"
echo "End Time: $end"
echo "$start $end" >> "$logfile"
/home/tawishi/Desktop/t./Daily-script/venv/bin/python3 /home/tawishi/Desktop/t./Daily-script/calculateTodaysFocusTime.py

