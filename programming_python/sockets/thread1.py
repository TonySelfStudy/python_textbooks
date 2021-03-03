import _thread
import time


def child(tid):
    print(f'Hello from thread: {tid}')
    for i in range(10):
        time.sleep(1)
        print(f'\t Thread: {tid} loop: {i}')


def parent():
    i = 0
    while True:
        i += 1
        _thread.start_new_thread(child, (i,))
        if input() == 'q': break


parent()
