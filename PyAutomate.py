import webbrowser
import time
import os
from datetime import datetime
from dotenv import load_dotenv

flag = load_dotenv()

alt = ""
if not flag:
    alt = "https://www.google.com/"

'''
Utility functions
'''
def continueDay():
    cont = input("Press ENTER to continue")

def printMessage(message=""):
    print(message)
    time.sleep(1)

'''
Start here
'''
os.system("bash logSystemOnOff.sh")

# mail
printMessage("Check mail")
webbrowser.open(os.getenv("MAIL",alt))
continueDay()
# calender
printMessage("Check your calendar")
webbrowser.open(os.getenv("CAL",alt))
# notion
printMessage("Update Daily Tasks")
webbrowser.open_new_tab(os.getenv("NOTION",alt))
continueDay()

# start touch type measure and practice
printMessage("test 1")
webbrowser.open(os.getenv("TEST1",alt))
continueDay()
printMessage("test 2")
webbrowser.open(os.getenv("TEST2",alt))
continueDay()
printMessage("test 3")
webbrowser.open(os.getenv("TEST3",alt))
continueDay()

# update daily type progess
printMessage("WPM daily update")
# subprocess.Popen('C:\\Windows\\System32\\calc.exe')
webbrowser.open(os.getenv("T_WORKSHEET",alt))
continueDay()

#JS stream
printMessage("Hi Mika!")
webbrowser.open(os.getenv("JS",alt))
continueDay()

# anki
printMessage("Anki time!")
webbrowser.open(os.getenv("ANKI",alt))
continueDay()

# Striver & Grind 75 & CSES
printMessage("Striver Sheet")
webbrowser.open(os.getenv("SS",alt))
continueDay()
printMessage("Grind")
webbrowser.open(os.getenv("GRIND_75",alt))
continueDay()

# leetcode
printMessage("Freq q.'s")
webbrowser.open(os.getenv("G",alt))
continueDay()

# CP
printMessage("CSES")
webbrowser.open(os.getenv("CSES",alt))
continueDay()

printMessage("Let's begin the day, Tawishi :) !")


