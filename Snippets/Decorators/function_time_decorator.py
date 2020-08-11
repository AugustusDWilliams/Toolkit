from time import time


def logtime(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        total_ms = end_time - start_time
        seconds = total_ms * 1000
        print("Total Time:", seconds)
        return result
    return wrapper


def execution_time(func):
    def timed(*args, **kwargs):
        time_start = time()
        return_value = func(*args, **kwargs)
        time_end = time()
        exec_time = time_end - time_start
        time_milliseconds = str(exec_time * 1000)
        arguments = [str(arg) for arg in args]
        keyword_arguments = ["{}={}".format(k, kwargs[k]) for k in kwargs]
        func_arguments = ", ".join(arguments + keyword_arguments)
        exec_time_str = "{}({}) exectued in {} ms".format(
            func.__name__, func_arguments, time_milliseconds
        )
        print(exec_time_str)
        return return_value

    return timed

def timethis(func):
    def wrapper(*args, **kwargs):
        start = time()
        res = func(*args,**kwargs)
        end = time()
        print('%s.%s: %f' % (func.__module__, func.__name__, end-start))
        return res
    return wrapper

@execution_time
def repeat(number, n_repeats=30000):
    return [number for number in range(30000)]


@logtime
# @execution_time
def sample_time_func():
    print("this is a sample_functon")


class Example:
    def __init__(self):
        super().__init__()

    @timethis
    def sample_func(self):
        print("This is a sample class function")

    @timethis
    def countdown(self, n):
        while n > 0:
            n -= 1
        return "Finished"


if __name__ == "__main__":
    # repeat(9)
    # repeat(20, 40000)
    # repeat(1, n_repeats=4000)
    # sample_time_func()
    example = Example()
    example.sample_func()
    example.countdown(1000000)
