from sympy import primerange
from threading import Thread
import random


class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)

    def join(self, *args):
        Thread.join(self, *args)
        return self._return


def rand_prime(n: int):
    min_ = pow(2, n - 1)
    max_ = pow(2, n) - 1
    return random.choice(list(primerange(min_, max_)))


def find_primitive_root(p: int):
    r = set(range(1, p))
    roots = []
    for i in r:
        gen = set()
        for x in r:
            gen.add(pow(i, x, p))
        if gen == r:
            roots.append(i)
            if len(roots) > 10:
                break
    result = random.choice(roots)
    return roots, result


def rand_n(n: int):
    # bits to decimal
    min_ = pow(2, n - 1)
    max_ = pow(2, n) - 1
    return random.randint(min_, max_)


def calc_key(key, g, p):
    return (g ** key) % p


def find_secret_key(a, b, p, g):
    a_, b_ = None, None
    for x in range(1, p):
        if calc_key(x, g, p) == a:
            a_ = x
        if calc_key(x, g, p) == b:
            b_ = x
    return a_, b_
