import time

"""
time countdown hatch
"""

def do_something():
    print('doing something')

do_something()

remaining_time = 10
break_time = 3
start_time = time.time()

while remaining_time > 0:
    time_elapsed = time.time() - start_time
    if time_elapsed < break_time:
        time.sleep(1)
        continue
    else:
        start_time = time.time()
        do_something()
        remaining_time -= time_elapsed
  
        
