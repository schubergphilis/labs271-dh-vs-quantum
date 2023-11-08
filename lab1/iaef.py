# Script that performs all calculations by prompting the user for the number
# of bits to be used to generate p, a and b.

import random
import time
from sympy import primerange
from threading import Thread
from colorama import Fore, Style


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


def _inputInt(message):
    userInput = input(message)
    try:
        result = int(userInput)
    except ValueError:
        print(userInput, "is not a valid integer")
        exit(1)
    return result


def _calcKey(key, g, p):
    return (g ** key) % p


def _findSecretKey(A, B, p, g):
    a, b = None, None
    for x in range(1, p):
        if (g ** x) % p == A:
            a = x
        if (g ** x) % p == B:
            b = x
    return a, b


def _randN(N):
    # bits to decimal
    min = pow(2, N-1)
    max = pow(2, N) - 1
    return random.randint(min, max)


def _isPrime(N: int):
    # check if integer is prime
    if N <= 1:
        return False
    for i in range(2, int(N**0.5) + 1):
        if (N % i) == 0:
            return False
    else:
        return True


def _randPrime(N: int):
    min = pow(2, N - 1)
    max = pow(2, N) - 1
    primeArray = list(primerange(min, max))
    return random.choice(primeArray)


def _findPrimitiveRoot(p):
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
    return random.choice(roots)


def _isDone():
    print(Style.RESET_ALL, "done")
    print("")
    input("Press Enter to continue...")
    print("")


def _pBlue(str):
    return (Fore.BLUE + str + Style.RESET_ALL)


def _pRed(str):
    return (Fore.RED + str + Style.RESET_ALL)


def _pGreen(str):
    return (Fore.GREEN + str + Style.RESET_ALL)


def _pYellow(str):
    return (Fore.YELLOW + str + Style.RESET_ALL)


def _pMagenta(str):
    return (Fore.MAGENTA + str + Style.RESET_ALL)


def _checkAnswer(title, userAnswer, Answer):
    print(title)
    if (userAnswer == Answer):
        print("  Congratulations!", _pGreen(str(Answer)),
              "is indeed the correct answer!")
    else:
        print("  Sorry, but", _pRed(str(userAnswer)), "is wrong,",
              _pGreen(str(Answer)), "is the correct answer.")


def main():
    print("INTRODUCTION")
    print("This program will show the steps involved in creating a shared ",
          "secret using the Diffie Hellman algorithm between two parties.")
    print("In this example the parties are Alice and Bob, ",
          "a well-known couple in Cryptography")
    print("Overview of all the steps:")
    print(_pGreen("Alice"), "will")
    print("  generate her private key", _pBlue("(a)"))
    print("  generate public prime number", _pBlue("(p)"))
    print("  calculate base key", _pBlue("(g)"),
          "as a primitive root modulo of", _pBlue("(p)"))
    print("  calculate her public key", _pBlue("(A)"),
          "using the following formula:", _pYellow("(g)^(a) MOD (p)"))
    print("  share", _pBlue("(g), (p)"), "and her public key",
          _pBlue("(A)"), "with", _pGreen("Bob"))
    print(_pGreen("Bob"), "will")
    print("  generate his private key", _pBlue("(b)"))
    print("  calculate his public key", _pBlue("(B)"),
          "using the following formula:", _pYellow("(g)^(b) MOD (p)"))
    print("  share his public key", _pBlue("(B)"), "with", _pGreen("Alice"))
    print(_pGreen("Alice and Bob"), "will use")
    print("   their private key", _pBlue("(a or b)"), "; and")
    print("   each others public key", _pBlue("(A or B)"), "; and")
    print("   the shared public prime number", _pBlue("(p)"))
    print("   to calculate their shared secret key", _pBlue("(k)"),
          "using the following formula:",
          _pYellow("(a or b)^(A or B) MOD (p)"))
    _isDone()

    print("It should be obvious that the longer the keys, ",
          "the harder the challenge to either calculate ",
          "(or break) Diffie Hellman.")
    print("This program will challenge you to a competition ",
          "in finding the shared secret", _pBlue("(k)"), "of",
          _pGreen("Alice and Bob"))
    print("The program will therefore")
    print("  generate random", _pBlue("a,b and p"), "; and")
    print("  calculate", _pBlue("g,A,B and k"))
    print("")
    print("Let's agree a bit size (>3) for the random generated keys")
    print(Fore.WHITE + "")
    keyLength = _inputInt("What bit size are you going to try and break: ")
    if (keyLength < 4):
        exit(0)
    print("")
    print(_pYellow("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"))
    print("Hint: In decimals, the generated keys")
    print("and prime number will be")
    print("  bigger than", (pow(2, keyLength-1)))
    print("  smaller than", (pow(2, keyLength)-1))
    print(_pYellow("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"))
    _isDone()

    print(_pGreen("Alice"))
    print("  generates public prime key", _pBlue("(p)"), "and public base key",
          _pBlue("(g)"), "...")
    pubBaseKey = -1
    while (pubBaseKey < 0):
        pubPrimeKey = _randPrime(keyLength)
        pubBaseKey = _findPrimitiveRoot(pubPrimeKey)
    print("    done")
    print(_pGreen("Alice and Bob"))
    print("  both generate their secret key", _pBlue("(a, b)"), "... ")
    privA = _randN(keyLength)
    privB = privA
    while (privA == privB):
        privB = _randN(keyLength)
    print("    done")
    print("  and keep them secret, even from Mallory in this program ",
          "(honest! check my source code :P)")
    _isDone()

    print(_pGreen("Alice"))
    print("  shares with", _pGreen("Bob"), "public base key",
          _pBlue("(g)"), ":",
          _pBlue(str(pubBaseKey)), "and public prime number",
          _pBlue("(p)"), ":",
          _pBlue(str(pubPrimeKey)), "...")
    _isDone()

    print(_pGreen("Alice and Bob"))
    print("  use their private keys", _pBlue("(a, b)"), ";and")
    print("  the public prime number", _pBlue("(p)"), ":",
          _pBlue(str(pubPrimeKey)))
    print("  the public base number", _pBlue("(g)"), ":",
          _pBlue(str(pubBaseKey)))
    print("  to calculate their public key", _pBlue("(A, B)"), "...", end="")
    thr_pubA = ThreadWithReturnValue(target=_calcKey,
                                     args=(privA, pubBaseKey, pubPrimeKey,))
    thr_pubA.start()
    thr_pubB = ThreadWithReturnValue(target=_calcKey,
                                     args=(privB, pubBaseKey, pubPrimeKey,))
    thr_pubB.start()
    pubA = thr_pubA.join()
    pubB = thr_pubB.join()
    print("    done")

    print("  exchange their public keys", _pBlue("(A, B)"), ":",
          _pBlue(str(pubA)), "and", _pBlue(str(pubB)))
    print("  Alice uses Bob's public key", _pBlue("(B)"), ":",
          _pBlue(str(pubB)),
          "to calculate their shared secret", _pBlue("(k)"), "...")
    thr_kA = ThreadWithReturnValue(target=_calcKey,
                                   args=(privA, pubB, pubPrimeKey,))
    thr_kA.start()
    print("  Bob uses Alice's public key", _pBlue("(A)"), ":",
          _pBlue(str(pubA)),
          "to calculate their shared secret", _pBlue("(k)"), "...")
    thr_kB = ThreadWithReturnValue(target=_calcKey,
                                   args=(privB, pubA, pubPrimeKey,))
    thr_kB.start()
    kA = thr_kA.join()
    kB = thr_kB.join()
    _isDone()

    print("Trusted Computer")
    print("  Checks if Alice and Bob have indeed the same shared secret",
          _pBlue("(k)"), "...")
    if (kA != kB):
        print("   ", _pRed("ERROR"), ": shared secret", _pBlue("(k)"),
              "is not the same")
        exit(1)
    else:
        print("   ", _pGreen("SUCCES"),
              "Alice and Bob have indeed calculated ",
              "the same secret", _pBlue("(k)"))
    _isDone()

    print("Now comes the time to test Malory, ",
          "a program to try and find Alice and Bob secret keys...")
    print("Regular CPU", _pMagenta("Mallory"),
          "will try to find either")
    print("  ", _pGreen("Alice's"), "secret key", _pBlue("(a)"), "; or")
    print("  ", _pGreen("Bob's"), "secret key", _pBlue("(b)"), "; or")
    print("  their shared secret", _pBlue("(k)"))
    print("Using")
    print("  the public prime number", _pBlue("(p)"), ":",
          _pBlue(str(pubPrimeKey)))
    print("  the public base number", _pBlue("(g)"), ":",
          _pBlue(str(pubBaseKey)))
    print("  Alice's public key", _pBlue("(A)"), ":", _pBlue(str(pubA)))
    print("  Bob's public key", _pBlue("(B)"), ":", _pBlue(str(pubB)))
    print("Press ENTER to start the challenge")
    _isDone()

    tic = time.perf_counter()
    print(_pMagenta("Mallory"))
    print("  tries to calculate Alice's and Bob's private key",
          _pBlue("(a, b)"),
          "using public known",
          _pBlue("(A), (B), (p) and (g)"),
          "... ")
    malPrivKeyA, malPrivKeyB = _findSecretKey(pubA, pubB,
                                              pubPrimeKey, pubBaseKey)
    print("    done")
    print("  calculates the secret key", _pBlue("(k)"), "of ",
          _pGreen("Alice and Bob"), "using the derived shared secrets",
          _pBlue("(a,b)"), "and publicly known",
          _pBlue("(A), (B), (p)"), "... ")
    thr_malSecretKeyA = ThreadWithReturnValue(target=_calcKey,
                                              args=(malPrivKeyA, pubB,
                                                    pubPrimeKey,))
    thr_malSecretKeyA.start()
    thr_malSecretKeyB = ThreadWithReturnValue(target=_calcKey,
                                              args=(malPrivKeyB, pubA,
                                                    pubPrimeKey,))
    thr_malSecretKeyB.start()
    malSecretKeyA = thr_malSecretKeyA.join()
    malSecretKeyB = thr_malSecretKeyB.join()
    print("    done")

    toc = time.perf_counter()
    print(f"  used {toc - tic:0.4f} seconds to complete the task")
    print("What did Mallory find?")
    _checkAnswer("Alice's Private Key", malPrivKeyA, privA)
    _checkAnswer("Bob's Private Key", malPrivKeyB, privB)
    _checkAnswer("Alice & Bob shared secret using Alice's private key",
                 malSecretKeyA, kA)
    _checkAnswer("Alice & Bob shared secret using Bob's private key",
                 malSecretKeyB, kB)
    print("NOTE: Their might be collisions (duplicate) private keys",
          _pBlue("(a or b)"),
          "but knowing the shared secret would already be a massive gain")


if __name__ == '__main__':
    main()
