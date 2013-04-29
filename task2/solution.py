from functools import reduce, lru_cache


def groupby(func, seq):
    res = reduce(lambda group, item: group.setdefault(func(item), [])
                 .append(item) or group, (item for item in seq), {})
    return res


def iterate(func):
    counter = 0
    func_composer = lambda count: reduce(lambda f, g: lambda x:
                                         f(g(x)), [func]*count)

    def identity(*args, **kwargs):
        if len(args) > 1:
            return args
        else:
            return args[0]

    while True:
        if not counter:
            yield identity
        else:
            yield func_composer(counter)

        counter += 1


def zip_with(func, *iterables):
    for args in zip(*iterables):
        yield func(*args)


def cache(func, cache_size):
    @lru_cache(cache_size)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper
