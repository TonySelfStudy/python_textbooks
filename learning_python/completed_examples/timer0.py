import time
import mytimer


def timer(func, *args):
    a = dir(timer)
    b = dir(func)

    # print('id, timer,   func')
    # for i in range(len(a)):
    #     if i < len(b):
    #         print(f'[{i}] {a[i]}, {b[i]}')
    #     else:
    #         print(f'[{i}] {a[i]}, ---')

    start_perf = time.perf_counter()
    # start_proc = time.process_time()
    for i in range(10_000):
        func(*args)
    print(f'Walk clock time: {time.perf_counter() - start_perf}')
    # print(f'Process time   : {time.process_time() - start_proc}')
    return


# timer(pow, 2, 1_000)
# timer(str.upper, 'spam')

tot1 = mytimer.total(10_000, pow, 2, 1000)[0]
tot2 = mytimer.total(10_000, str.upper, 'spam')[0]
best1 = mytimer.bestof(10_000, str.upper, 'spam')[0]
print(tot1)
print(tot2)
print(best1 * 10_000)

print(mytimer.bestoftotal(500, 1000, str.upper, 'spam'))
