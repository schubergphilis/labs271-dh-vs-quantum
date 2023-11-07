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


def _inputInt(message, input_type=int):
    while True:
        try:
            return input_type(input(message))
        except:
            pass


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


def randN(N):
    # bits to decimal
    min = pow(2, N-1)
    max = pow(2, N) - 1
    return random.randint(min, max)


def isPrime(N: int):
    # check if integer is prime
    if N <= 1:
        return False
    for i in range(2, int(N**0.5) + 1):
        if (N % i) == 0:
            return False
    else:
        return True


def randPrime(N: int):
    min = pow(2, N - 1)
    max = pow(2, N) - 1
    primeArray = list(primerange(min, max))
    return random.choice(primeArray)


def findPrimitive(theNum):
    o = 1
    roots = []
    r = 2
    while r < theNum:
        k = pow(r, o, theNum)
        while (k > 1):
            o = o + 1
            k = (k * r) % theNum
        if o == (theNum - 1):
            roots.append(r)
        o = 1
        r = r + 1
    return random.choice(roots)


def isDone():
    print(Style.RESET_ALL, "done")
    print("")
    input("Press Enter to continue...")
    print("")


def pBlue(str):
    return (Fore.BLUE + str + Style.RESET_ALL)


def pRed(str):
    return (Fore.RED + str + Style.RESET_ALL)


def pGreen(str):
    return (Fore.GREEN + str + Style.RESET_ALL)


def pYellow(str):
    return (Fore.YELLOW + str + Style.RESET_ALL)


def pMagenta(str):
    return (Fore.MAGENTA + str + Style.RESET_ALL)


def checkAnswer(title, userAnswer, Answer):
    print(title)
    if (userAnswer == Answer):
        print("  Congratulations!", pGreen(str(Answer)),
              "is indeed the correct answer!")
    else:
        print("  Sorry, but", pRed(str(userAnswer)), "is wrong,",
              pGreen(str(Answer)), "is the correct answer.")


def main():
    print("INTRODUCTION")
    print("This program will show the steps involved in creating a shared ",
          "secret using the Diffie Hellman algorithm between two parties.")
    print("In this example the parties are Alice and Bob, ",
          "a well-known couple in Cryptography")
    print("Overview of all the steps:")
    print(pGreen("Alice"), "will")
    print("  generate her private key", pBlue("(a)"))
    print("  generate public prime number", pBlue("(p)"))
    print("  calculate base key", pBlue("(g)"),
          "as a primitive root modulo of", pBlue("(p)"))
    print("  calculate her public key", pBlue("(A)"),
          "using the following formula:", pYellow("(g)^(a) MOD (p)"))
    print("  share", pBlue("(g), (p)"), "and her public key",
          pBlue("(A)"), "with", pGreen("Bob"))
    print(pGreen("Bob"), "will")
    print("  generate his private key", pBlue("(b)"))
    print("  calculate his public key", pBlue("(B)"),
          "using the following formula:", pYellow("(g)^(b) MOD (p)"))
    print("  share his public key", pBlue("(B)"), "with", pGreen("Alice"))
    print(pGreen("Alice and Bob"), "will use")
    print("   their private key", pBlue("(a or b)"), "; and")
    print("   each others public key", pBlue("(A or B)"), "; and")
    print("   the shared public prime number", pBlue("(p)"))
    print("   to calculate their shared secret key", pBlue("(k)"),
          "using the following formula:", pYellow("(a or b)^(A or B) MOD (p)"))
    isDone()

    print("It should be obvious that the longer the keys, ",
          "the harder the challenge to either calculate ",
          "(or break) Diffie Hellman.")
    print("This program will challenge you to a competition ",
          "in finding the shared secret", pBlue("(k)"), "of",
          pGreen("Alice and Bob"))
    print("The program will therefore")
    print("  generate random", pBlue("a,b and p"), "; and")
    print("  calculate", pBlue("g,A,B and k"))
    print("")
    print("Let's agree a bit size (>3) for the random generated keys")
    print(Fore.WHITE + "")
    keyLength = _inputInt(
        "What bit size are you going to try and break: ", int)
    if (keyLength < 4):
        exit(0)
    print("")
    print(pYellow("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"))
    print("Hint: In decimals, the generated keys")
    print("and prime number will be")
    print("  bigger than", (pow(2, keyLength-1)))
    print("  smaller than", (pow(2, keyLength)-1))
    print(pYellow("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"))
    isDone()

    print(pGreen("Alice"))
    print("  generates public base key", pBlue("(g)"), "and public prime key",
          pBlue("(p)"), "...")
    pubBaseKey = -1
    while (pubBaseKey < 0):
        pubPrimeKey = randPrime(keyLength)
        pubBaseKey = findPrimitive(pubPrimeKey)
    print("    done")
    print(pGreen("Alice and Bob"))
    print("  both generate their secret key", pBlue("(a, b)"), "... ")
    privA = randN(keyLength)
    privB = privA
    while (privA == privB):
        privB = randN(keyLength)
    print("    done")
    print("  and keep them secret, even from Mallory in this program ",
          "(honest! check my source code :P)")
    isDone()

    print(pGreen("Alice"))
    print("  shares with", pGreen("Bob"), "public base key", pBlue("(g)"), ":",
          pBlue(str(pubBaseKey)), "and public prime number", pBlue("(p)"), ":",
          pBlue(str(pubPrimeKey)), "...")
    isDone()

    print(pGreen("Alice and Bob"))
    print("  use their private keys", pBlue("(a, b)"), ";and")
    print("  the public prime number", pBlue("(p)"), ":",
          pBlue(str(pubPrimeKey)))
    print("  the public base number", pBlue("(g)"), ":",
          pBlue(str(pubBaseKey)))
    print("  to calculate their public key", pBlue("(A, B)"), "...", end="")
    thr_pubA = ThreadWithReturnValue(target=calcKey,
                                     args=(privA, pubBaseKey, pubPrimeKey,))
    thr_pubA.start()
    thr_pubB = ThreadWithReturnValue(target=calcKey,
                                     args=(privB, pubBaseKey, pubPrimeKey,))
    thr_pubB.start()
    pubA = thr_pubA.join()
    pubB = thr_pubB.join()
    print("    done")

    print("  exchange their public keys", pBlue("(A, B)"), ":",
          pBlue(str(pubA)), "and", pBlue(str(pubB)))
    print("  Alice uses Bob's public key", pBlue("(B)"), ":", pBlue(str(pubB)),
          "to calculate their shared secret", pBlue("(k)"), "...")
    thr_kA = ThreadWithReturnValue(target=calcKey,
                                   args=(privA, pubB, pubPrimeKey,))
    thr_kA.start()
    print("  Bob uses Alice's public key", pBlue("(A)"), ":", pBlue(str(pubA)),
          "to calculate their shared secret", pBlue("(k)"), "...")
    thr_kB = ThreadWithReturnValue(target=calcKey,
                                   args=(privB, pubA, pubPrimeKey,))
    thr_kB.start()
    kA = thr_kA.join()
    kB = thr_kB.join()
    isDone()

    print("Trusted Computer")
    print("  Checks if Alice and Bob have indeed the same shared secret",
          pBlue("(k)"), "...")
    if (kA != kB):
        print("   ", pRed("ERROR"), ": shared secret", pBlue("(k)"),
              "is not the same")
        exit(1)
    else:
        print("   ", pGreen("SUCCES"), "Alice and Bob have indeed calculated ",
              "the same secret", pBlue("(k)"))
    isDone()

    print("Now comes the time to test Malory, ",
          "a program to try and find Alice and Bob secret keys...")
    print("Regular CPU", pMagenta("Mallory"),
          "will try to find either")
    print("  ", pGreen("Alice's"), "secret key", pBlue("(a)"), "; or")
    print("  ", pGreen("Bob's"), "secret key", pBlue("(b)"), "; or")
    print("  their shared secret", pBlue("(k)"))
    print("Using")
    print("  the public prime number", pBlue("(p)"), ":",
          pBlue(str(pubPrimeKey)))
    print("  the public base number", pBlue("(g)"), ":",
          pBlue(str(pubBaseKey)))
    print("  Alice's public key", pBlue("(A)"), ":", pBlue(str(pubA)))
    print("  Bob's public key", pBlue("(B)"), ":", pBlue(str(pubB)))
    print("Press ENTER to start the challenge")
    isDone()

    tic = time.perf_counter()
    print(pMagenta("Mallory"))
    print("  tries to calculate Alice's and Bob's private key",
          pBlue("(a, b)"),
          "using public known",
          pBlue("(A), (B), (p) and (g)"),
          "... ")
    malPrivKeyA, malPrivKeyB = findSecretKey(pubA, pubB,
                                             pubPrimeKey, pubBaseKey)
    print("    done")
    print("  calculates the secret key", pBlue("(k)"), "of ",
          pGreen("Alice and Bob"), "using the derived shared secrets",
          pBlue("(a,b)"), "and publicly known", pBlue("(A), (B), (p)"), "... ")
    thr_malSecretKeyA = ThreadWithReturnValue(target=calcKey,
                                              args=(malPrivKeyA, pubB,
                                                    pubPrimeKey,))
    thr_malSecretKeyA.start()
    thr_malSecretKeyB = ThreadWithReturnValue(target=calcKey,
                                              args=(malPrivKeyB, pubA,
                                                    pubPrimeKey,))
    thr_malSecretKeyB.start()
    malSecretKeyA = thr_malSecretKeyA.join()
    malSecretKeyB = thr_malSecretKeyB.join()
    print("    done")

    toc = time.perf_counter()
    print(f"  used {toc - tic:0.4f} seconds to complete the task")
    print("What did Mallory find?")
    checkAnswer("Alice's Private Key", malPrivKeyA, privA)
    checkAnswer("Bob's Private Key", malPrivKeyB, privB)
    checkAnswer("Alice & Bob shared secret using Alice's private key",
                malSecretKeyA, kA)
    checkAnswer("Alice & Bob shared secret using Bob's private key",
                malSecretKeyB, kB)
    print("NOTE: Their might be collisions (duplicate) private keys",
          pBlue("(a or b)"),
          "but knowing the shared secret would already be a massive gain")


if __name__ == '__main__':
    main()
