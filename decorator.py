# Decorators
from functools import wraps
import time

class decorator_timer(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        t1 = time.time()
        result = self.original_function(*args, **kwargs)
        print('{} ran in: {} sec'.format(self.original_function.__name__, time.time() - t1))
        print('call method executed this before {}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info('Ran with args {}, and kwargs: {}'.format(args, kwargs))

        return orig_func(*args, **kwargs)
    return wrapper

def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result
    return wrapper

@decorator_timer
def random_x():
    a = []
    for x in range(1000000):
        a.append(x)
    return a

random_x()
