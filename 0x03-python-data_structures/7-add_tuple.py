#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    if (tuple_a is None):
        tuple_a = ()
    if (tuple_b is None):
        tuple_b = ()
    sum = [0, 0]
    for i in range(2):
        try:
            sum[i] += tuple_a[i]
        except Exception as e:
            sum[i] += 0
        try:
            sum[i] += tuple_b[i]
        except Exception as e:
            sum[i] += 0
    return (sum[0], sum[1])
