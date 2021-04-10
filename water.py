#!/bin/python3
#################################################################
# Macosx only.                                                  #
# Changes message, title, timing, source, sound just be happy.  #
# Usage: nohup python3 drink-water.py &                         #
#################################################################
import subprocess
import time

command = '''
on run argv
  display notification (item 2 of argv) with title (item 1 of argv)
end run
'''


def notify():
    _title = "Hora de ficar mais saudável"
    _message = "Levante e beba um copo de aguá."
    while True:
        call_system(['afplay', '/System/Library/Sounds/Glass.aiff'])
        call_system(['osascript', '-e', command, _title, _message])
        time.sleep(300)


def call_system(cmd):
    subprocess.call(cmd)


if __name__ == '__main__':
    notify()
