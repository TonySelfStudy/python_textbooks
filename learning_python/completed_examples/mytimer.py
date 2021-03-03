from time import perf_counter as timer

def total(reps, func, *args, **kargs):

    replist = list(range(reps))
    start = timer()
    for i in replist:
        ret = func(*args, **kargs)
    elapsed = timer() - start
    return elapsed, ret


def bestof(reps, func, *args, **kargs):
    best = 2 ** 32
    for i in range(reps):
        start = timer()
        ret = func(*args, **kargs)
        elapsed = timer() - start
        if elapsed < best:
            best = elapsed
    return best, ret


def bestoftotal(reps1, reps2, func, *args, **kargs):
    print(f'bestoftotal called with the following args')
    print(locals())

    return bestof(reps1, total, reps2, func, *args, **kargs)

