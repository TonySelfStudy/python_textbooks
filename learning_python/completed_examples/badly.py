import traceback
from inspectors import Inspector
from sys import exc_info

def inverse(x):
    return 1 / x

try:
    inverse(0)
except Exception:
    insp = Inspector()
    insp = Inspector()
    insp.climb_dir(exc_info, None)
    insp.climb_dir(traceback, None)
    traceback.print_exc(file=open('badly.exc', 'w'))
print('Bye')
