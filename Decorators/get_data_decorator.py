import time
import functools
from loguru import logger


def get_data(data_size=1):
    def decorator(func):
        def wrap(*args, **kwargs):
            try:
                res = func(*args, **kwargs)
            except Exception as err:
                print(err)
                if data_size == 1:
                    res = ""
                else:
                    res = [""] * data_size
            finally:
                return res
        return wrap
    return decorator

class Sample:z
    def __init__(self):
        self.val = 7
        self.data = {"val1": "1",
                     "val2": 2}

    #@get_data(is_array=True)
    def func(self, key):
        logger.debug('In Class Function')
        logger.debug("The passed in arugment is:", key)

    @get_data()
    def get_val(self, g=False):
        val = 1
        return val

@get_data(3)
def classless_func(val):
    return val / 0

if __name__ == "__main__":
    obj = Sample()
    #obj.func('7')
    res = obj.get_val(7)
    print(res)
    print(classless_func(5))
