import psutil

def check_process_exists(process_name):
    for proc in psutil.process_iter(['pid']):
	    print(proc)
	    if proc.info['pid'] == process_pid:
	    	return True
    return False


# Example usage
"""
process_pid =  "10002"
exists = check_process_exists(process_pid)
if exists:
    print(f"Process '{process_pid}' is running.")
else:
    print(f"Process '{process_pid}' is not running.")
"""
