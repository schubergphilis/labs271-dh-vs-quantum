from argparse import ArgumentParser
from math import sqrt
import random
import time
from threading import Thread
from colorama import Fore

def _inputInt(message, input_type=int):
  while True:
    try:
      return input_type (input(message))
    except:pass

def calcKey(key, g, p):
   return (g ** key) % p

class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args,
                                                **self._kwargs)
    def join(self, *args):
        Thread.join(self, *args)
        return self._return

def findSecretKey(A, B, p, g):
    a, b = None, None
    for x in range(1, p):
        print("#", end="")
        if (g ** x) % p == A:
            a = x
        if (g ** x) % p == B:
            b = x
    return a, b

def randN(N):
    #bits to decimal
    min = pow(2, N-1)
    max = pow(2, N) - 1
    return random.randint(min, max)

def isPrime(N:int):
    if N <= 1:
        return False
    for i in range(2, int(N**0.5) + 1):
        if (N % i) == 0:
            return False
    else:
        return True

def randPrime(N:int):
    result=0
    while not isPrime(result):
        result = randN(N)
    return result


def findPrimeFactors(s, n):
    # Print the number of 2s that divide n
    while (n % 2 == 0) :
        s.add(2)
        n = n // 2
    # n must be odd at this point. So we can
    # skip one element (Note i = i +2)
    for i in range(3, int(sqrt(n)), 2):
        # While i divides n, print i and divide n
        while (n % i == 0):
            s.add(i)
            n = n // i
    # This condition is to handle the case
    # when n is a prime number greater than 2
    if (n > 2) :
        s.add(n)

def power( x, y, p):
    res = 1 # Initialize result
    x = x % p # Update x if it is more
              # than or equal to p
    while (y > 0):
        # If y is odd, multiply x with result
        if (y & 1):
            res = (res * x) % p
        # y must be even now
        y = y >> 1 # y = y/2
        x = (x * x) % p
    return res

def findPrimitive( n) :
    s = set()
    # Find value of Euler Totient function
    # of n. Since n is a prime number, the
    # value of Euler Totient function is n-1
    # as there are n-1 relatively prime numbers.
    phi = n - 1
    # Find prime factors of phi and store in a set
    findPrimeFactors(s, phi)
    # Check for every number from 2 to phi
    for r in range(2, phi + 1):
        # Iterate through all prime factors of phi.
        # and check if we found a power with value 1
        flag = False
        for it in s:
            # Check if r^((phi)/primefactors)
            # mod n is 1 or not
            if (power(r, phi // it, n) == 1):
                flag = True
                break
        # If there was no power with value 1.
        if (flag == False):
            return r
    # If no primitive root found
    return -1

def isDone():
    print (Fore.WHITE+"done")
    print ("")
    input("Press Enter to continue...")
    print ("")

def checkAnswer(title, userAnswer, Answer):
    print (title)
    if (userAnswer == Answer):
        print ("  Congratulations!",Answer,"is indeed the correct answer!")
    else:
        print ("  Sorry, but",userAnswer, "is wrong,",Answer,"is the correct answer.")

def main():
    parser = ArgumentParser()
    print("Overview of all the steps:")
    print(Fore.GREEN + "Alice will")
    print((Fore.WHITE + "  generate her private key"),(Fore.BLUE + "(a)"))
    print((Fore.WHITE + "  generate public prime number"),(Fore.BLUE + "(p)"))
    print((Fore.WHITE + "  calculate base key"),(Fore.BLUE + "(g)"),(Fore.WHITE + "as a primitive root modulo of"),(Fore.BLUE + "(p)"))
    print((Fore.WHITE + "  calculate her public key (pubA) using the following formula:"),(Fore.YELLOW + "(g)^(a) MOD (p)"))
    print((Fore.WHITE + "  share"),(Fore.BLUE + "(g), (p)"),(Fore.WHITE + "and her public key"),(Fore.BLUE + "(pubA)"),(Fore.WHITE + "with"),(Fore.GREEN + "Bob"))
    isDone()
    print(Fore.GREEN + "Bob will")
    print((Fore.WHITE + "  generate his private key"),(Fore.BLUE + "(b)"))
    print((Fore.WHITE + "  calculate his public key"),(Fore.BLUE + "(pubB)"),(Fore.WHITE + "using the following formula:"),(Fore.YELLOW + "(g)^(b) MOD (p)"))
    print((Fore.WHITE + "  share his public key"),(Fore.BLUE + "(pubB)"),(Fore.WHITE + "with"),(Fore.GREEN + "Alice"))
    print((Fore.WHITE +"Using their private key"),(Fore.BLUE + "(a or b)"),(Fore.WHITE +"and each others public key"),(Fore.BLUE + "(pubA or pubB)"),(Fore.WHITE +","),(Fore.GREEN + "Alice and Bob"),(Fore.WHITE +"can calculate their shared secret key"),(Fore.BLUE + "(k)"))
    isDone()
    print("Let's perform the challenge...")
    print("The longer the key the harder the challenge to either calculate or break Diffie Hellman.")
    print("Let's agree a bit size (>4) for the publicBaseKey",(Fore.BLUE + "(g)"),(Fore.WHITE +", publicPrimeKey"),(Fore.BLUE + "(p)"),(Fore.WHITE +", privateKeyA"),(Fore.BLUE + "(A)"),(Fore.WHITE +"and privateKeyB"),(Fore.BLUE + "(B)"))
    print(Fore.WHITE +"")
    keyLength = _inputInt("What bit size are you going to try and break: ",int)
    if (keyLength<4):
        exit(0)
    print("")
    print("The generated keys and prime number will be bigger than",(pow(2, keyLength-1)),"and smaller than",(pow(2, keyLength)-1))
    print ("Alice")
    print ("  generates public base key (g) and public prime key (p)...")
    pubBaseKey = -1
    while (pubBaseKey < 0):
        pubPrimeKey = randPrime(keyLength)
        pubBaseKey = findPrimitive(pubPrimeKey)
    isDone()

    print("Alice and Bob")
    print("  both generate their secret key (a, b)...")
    privA = randN(keyLength)
    privB = randN(keyLength)
    isDone()

    print("Alice")
    print("  shares with Bob public base key (g):",pubBaseKey,"and public prime number (p):",pubPrimeKey,"...")
    isDone()

    print("Alice and Bob")
    print ("  calculate their public key (A, B) using their private keys (a, b), public base key (g):",pubBaseKey,"public prime number (p):",pubPrimeKey,"...")
    thr_pubA = ThreadWithReturnValue(target=calcKey, args=(privA, pubBaseKey, pubPrimeKey,))
    thr_pubA.start()
    thr_pubB = ThreadWithReturnValue(target=calcKey, args=(privB, pubBaseKey, pubPrimeKey,))
    thr_pubB.start()
    pubA = thr_pubA.join()
    pubB = thr_pubB.join()
    print ("  exchange their public keys (A, B):",pubA,"and",pubB)
    print ("  Alice uses Bob's public key (B):",pubB,"to calculate their shared secret (k)...")
    print ("  Bob uses Alice's public key (A):",pubA,"to calculate their shared secret (k)...")
    thr_kA = ThreadWithReturnValue(target=calcKey, args=(privA, pubB, pubPrimeKey,))
    thr_kA.start()
    thr_kB = ThreadWithReturnValue(target=calcKey, args=(privB, pubA, pubPrimeKey,))
    thr_kB.start()
    kA = thr_kA.join()
    kB = thr_kB.join()
    isDone()
    print ("Trusted Computer")
    print ("  Checks if Alice and Bob have indeed the same shared secret (k)...")
    if (kA!=kB):
        print ("    ERROR: shared secret k is not the same")
        exit(1)
    else:
        print ("    Alice and Bob have indeed calculated the same secret k")
    isDone()

    input("Press Enter to compete with CPU Mallory to find either Alice's secret key (a), or Bob's secret key (b) or shared secret (k)...")
    tic = time.perf_counter()
    print ("Mallory")
    print ("  Calculates the private keys of Alice and Bob using public known (A), (B), (p) and (g)")
    calcPrivKeyA, calcPrivKeyB = findSecretKey (pubA,pubB,pubPrimeKey,pubBaseKey)
    print ("  Done")
    print ("")
    print ("  Calculates the secret keys of Alice and Bob using the derived shared secret (k), public known (A), (B), (p) and (g)")
    thr_calcSecretKeyA = ThreadWithReturnValue(target=calcKey, args=(calcPrivKeyA, pubB, pubPrimeKey,))
    thr_calcSecretKeyA.join()
    thr_calcSecretKeyB = ThreadWithReturnValue(target=calcKey, args=(calcPrivKeyB, pubA, pubPrimeKey,))
    thr_calcSecretKeyB.join()
    calcSecretKeyA = thr_calcSecretKeyA.join()
    calcSecretKeyB = thr_calcSecretKeyB.join()
    isDone()
    toc = time.perf_counter()
    print(f" Mallory CPU calculated Alice's secret key (a) and Bob's secret key (b) and their shared secret key (k) in {toc - tic:0.4f} seconds")
    isDone()
    print("++++++++++++++++++++++++++++++++++++")
    print("Cheating secretKeyA:",privA)
    print("Cheating secretKeyB:",privB)
    print("Cheating sharedSecretA:",kA)
    print("Cheating sharedSecretB:",kB)
    print("++++++++++++++++++++++++++++++++++++")
    print ("")
    userCalc_PrivKeyA = _inputInt("What is your answer for Alices secret key (a): ")
    userCalc_PrivKeyB = _inputInt("What is your answer for Bob's secret key (b): ")
    userCalc_SecretKey = _inputInt("What is your answer for the shared secret (k): ")
    print ("Your answers:")
    checkAnswer("Alice's Private Key", userCalc_PrivKeyA, privA)
    checkAnswer("Bob's Private Key", userCalc_PrivKeyB, privB)
    checkAnswer("Alice & Bob shared secret", userCalc_SecretKey, kA)

    print("")
    print ("Did the Mallory do any better?")
    checkAnswer("Alice's Private Key", calcPrivKeyA, privA)
    checkAnswer("Bob's Private Key", calcPrivKeyB, privB)
    checkAnswer("Alice & Bob shared secret using Alice's private key", calcSecretKeyA, kA)
    checkAnswer("Alice & Bob shared secret using Bob's private key", calcSecretKeyB, kB)


if __name__ == '__main__':
    main()


