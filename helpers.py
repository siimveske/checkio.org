from timeit import default_timer as timer


def timeit(func, *args):
    start = timer()
    func(*args)
    end = timer()
    print("time elapsed in ", func.__name__, ": ", end - start, sep='')
