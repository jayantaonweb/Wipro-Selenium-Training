#threading - execution of task
# multithreading - execution of many task at the same time - concurrent execution
# multiprocessing

# Threading - imported


# process - execution unit
# thread - lightweight unit inside the process

# simple thread
import threading
import time


def task():
    print("thread started")
    time.sleep(2)
    print("Thread Finished")

t= threading.Thread(target= task)
t.start()
t.join()

print("Thread terminated")



