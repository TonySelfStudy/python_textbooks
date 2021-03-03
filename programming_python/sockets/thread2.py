import _thread
import time

child_count = 0

def child(my_list_c):
    global child_count
    child_num = child_count
    child_count += 1

    print(f'Hello from child: {child_num}')
    for i in range(10):
        time.sleep(1)
        print(f'\t Child: {child_num} loop: {i}')
        my_list_c.append((child_num, i))


def parent():
    my_list = []
    while True:
        _thread.start_new_thread(child, (my_list,))
        if input() == 'q': break
    print(my_list)

parent()
