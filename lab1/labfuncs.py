from sympy import primerange
from threading import Thread
import random


class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)

    def join(self, *args):
        Thread.join(self, *args)
        return self._return


def randPrime(N: int):
    min = pow(2, N - 1)
    max = pow(2, N) - 1
    primeArray = list(primerange(min, max))
    result = random.choice(primeArray)
    return result


def findPrimitiveRoot(p: int):
    r = set(range(1, p))
    roots = []
    for i in r:
        gen = set()
        for x in r:
            gen.add(pow(i, x, p))
        if gen == r:
            roots.append(i)
            if (len(roots) > 10):
                break
    result = random.choice(roots)
    return roots, result


def randN(N: int):
    # bits to decimal
    min = pow(2, N-1)
    max = pow(2, N) - 1
    return random.randint(min, max)


def calcKey(key, g, p):
    return (g ** key) % p


def findSecretKey(A, B, p, g):
    a, b = None, None
    for x in range(1, p):
        if (g ** x) % p == A:
            a = x
        if (g ** x) % p == B:
            b = x
    return a, b
