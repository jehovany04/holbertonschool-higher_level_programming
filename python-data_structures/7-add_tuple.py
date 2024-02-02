#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    r = [{i: v for i, v in enumerate(t)} for t in [tuple_a, tuple_b]]
    return tuple(sum([r[i].get(x, 0) for i in [0, 1]]) for x in [0, 1])
