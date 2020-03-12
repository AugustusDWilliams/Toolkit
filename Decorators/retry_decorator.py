import time
import random
import functools
from loguru import logger


def retry(func):
    functools.wraps(func)
    def wrapped_function(*args):
        attempt = 0
        max_attempts = 3
        delay = 1
        backoff = 2
        while attempt < max_attempts:
            try:
                return func(*args)
            except Exception as err:
                logger.debug("In Retry Decorator Attempt #", attempt)
                err_msg = '{}, Retrying in {} seconds...'.format(err, delay)
                logger.warning(err_msg)
                attempt += 1
                time.sleep(delay)
                delay *= backoff
        logger.error("Failed to Execute the function")
        return None
    return wrapped_function

@retry
def main_func():
    x = random.random()
    if x < 0.5:
        raise Exception("Fail")
    else:
        print ("Success")


if __name__ == "__main__":
    res = main_func()
    print(res)
