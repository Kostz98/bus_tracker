import subprocess
import time

while True:
    subprocess.call(['python', r'busTracker.py'])
    time.sleep(2)
