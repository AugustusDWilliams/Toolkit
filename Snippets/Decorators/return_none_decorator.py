def return_none(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            return None
    return wrapper

@return_none
def sample_func(val):
    return val / 0

if __name__ == "__main__":
    res = sample_func(7)
    print(res)