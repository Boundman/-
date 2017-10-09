import contextlib
import time

@contextlib.contextmanager
def timer():
    t = time.clock()
    yield
    print(time.clock() - t)
