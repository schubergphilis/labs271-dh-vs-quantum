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


def randPrime(name: str, N: int):
    min = pow(2, N - 1)
    max = pow(2, N) - 1
    primeArray = list(primerange(min, max))
    result = random.choice(primeArray)
    print(name, "set to:", result)
    return result


def findPrimitive(name: str, N: int):
    o = 1
    roots = []
    r = 2
    while r < N:
        k = pow(r, o, N)
        while (k > 1):
            o = o + 1
            k = (k * r) % N
        if o == (N - 1):
            roots.append(r)
        o = 1
        r = r + 1
    result = random.choice(roots)
    print(name, "set to:", result)
    return result


def randN(N):
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
