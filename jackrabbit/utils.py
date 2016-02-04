import collections
import sys

if sys.platform == 'win32':
    from time import clock as time
else:
    from time import time


def is_callable(o):
    return isinstance(o, collections.Callable)
