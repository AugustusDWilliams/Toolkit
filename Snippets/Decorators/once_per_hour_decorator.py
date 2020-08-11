import functools
from time import time


def once_per_minute(func):
    last_invoked = 0
    def wrapper(*args, **kwargs):
        nonlocal last_invoked
        elapsed_time = time() - last_invoked
        if elapsed_time < 60:
            #rasie CalledTooOftenError
            raise Exception("Only {} has passed".format(elapsed_time))
        last_invoked = time()
        return func(*args, **kwargs)
    return wrapper

@once_per_minute
def example():
    return "Example function ran successfully"


if __name__ == "__main__":
    print(example())
    print(example())
