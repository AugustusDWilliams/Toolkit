import timeit


def sample_func():
    print("Inside sample function.")


setup = "from __main__ import sample_func"
stmt = "sample_func()"
num = 7

timeit.timeit(setup=setup, stmt=stmt, number=num)
t = timeit.Timer(setup=setup, stmt=stmt)
r = t.timeit(num)
res = t.repeat(3, 2)
print(r)
print(res)