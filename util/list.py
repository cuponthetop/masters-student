import itertools


def find(pred, iterable):
    return next(itertools.ifilter(pred, iterable), None)