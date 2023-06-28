LANG=en_US.utf8

helperfile="/home/tawishi/Desktop/t./self_track/logs/keyfreqraw.txt" # temporary helper file

mkdir -p logs

while true
do
  showkey > $helperfile &
  PID=$!
  
  # work in windows of 9 seconds 
  sleep 9
  
  # check if process is running before killing it
	if kill -0 "$PID" >/dev/null 2>&1; then
		kill $PID
		#echo "Process with PID $pid is running."
	else
	    echo "Process with PID $pid is not running."
	fi
  
  # count number of key release events
  num=$(cat $helperfile | grep release | wc -l)
  timetag=$(python rewind7am.py)
  # append unix time stamp and the number into file
  logfile="/home/tawishi/Desktop/t./self_track/logs/keyfreq_$timetag.txt"
  echo "$(date +%s) $num"  >> $logfile
  echo "logged key frequency: $(date) $num release events detected into $logfile"
  
done

