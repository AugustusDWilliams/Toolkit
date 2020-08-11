import time
import functools
from loguru import logger


def function_decorator(func):
    functools.wraps(func)
    def wrapped_function(cls, *args):
        logger.debug('In Decorator')
        return func(cls, *args)
    return wrapped_function

class Sample:
    def __init__(self):
        self.val = 7

    @function_decorator
    def func(self, val):
        logger.debug('In Class Function')
        logger.debug("The passed in arugment is:", val)


if __name__ == "__main__":
    obj = Sample()
    obj.func('7')
