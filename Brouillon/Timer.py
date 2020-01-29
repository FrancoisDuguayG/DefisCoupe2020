import time
import sys
import threading

time_start = time.time()
seconds = 0
minutes = 2
paused = threading.Event()

while not paused.is_set():
    try:
        sys.stdout.write("\r{minutes} Minutes {seconds} Seconds".format(minutes=minutes, seconds=seconds))
        sys.stdout.flush()
        time.sleep(1)
        #seconds = int(time.time() - time_start) - minutes * 60
        if minutes > 0 or seconds > 0:
            if seconds <= 0:
                minutes -= 1
                seconds = 2
            else:
                seconds -= 1
        else:
            print("boomer")
            paused.set()

    except KeyboardInterrupt as e:
        break
