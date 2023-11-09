# Script that performs all calculations by prompting the user for the number
# of bits to be used to generate p, a and b.

import random
import time
from sympy import primerange
from threading import Thread
from colorama import Fore, Style


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


def _input_int(message):
    user_input = input(message)
    try:
        result = int(user_input)
    except ValueError:
        print(user_input, "is not a valid integer")
        raise SystemExit(1)
    return result


def _calc_key(key, g, p):
    return (g ** key) % p


def _find_secret_key(a, b, p, g):
    a_, b_ = None, None
    for x in range(1, p):
        if _calc_key(x, g, p) == a:
            a_ = x
        if _calc_key(x, g, p) == b:
            b_ = x
    return a_, b_


def _rand_n(n):
    # bits to decimal
    min_ = pow(2, n - 1)
    max_ = pow(2, n) - 1
    return random.randint(min_, max_)


def _is_prime(n: int):
    # check if integer is prime
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if (n % i) == 0:
            return False
    return True


def _rand_prime(n: int):
    min_ = pow(2, n - 1)
    max_ = pow(2, n) - 1
    return random.choice(list(primerange(min_, max_)))


def _find_primitive_root(p):
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
    return random.choice(roots)


def _is_done():
    print(Style.RESET_ALL, "done")
    print("")
    input("Press Enter to continue...")
    print("")


def _p_blue(str):
    return Fore.BLUE + str + Style.RESET_ALL


def _p_red(str):
    return Fore.RED + str + Style.RESET_ALL


def _p_green(str):
    return Fore.GREEN + str + Style.RESET_ALL


def _p_yellow(str):
    return Fore.YELLOW + str + Style.RESET_ALL


def _p_magenta(str):
    return Fore.MAGENTA + str + Style.RESET_ALL


def _check_answer(title, user_answer, answer):
    print(title)
    if user_answer == answer:
        print("  Congratulations!", _p_green(str(answer)),
              "is indeed the correct answer!")
    else:
        print("  Sorry, but", _p_red(str(user_answer)), "is wrong,",
              _p_green(str(answer)), "is the correct answer.")


def main():
    print("INTRODUCTION")
    print("This program will show the steps involved in creating a shared ",
          "secret using the Diffie Hellman algorithm between two parties.")
    print("In this example the parties are Alice and Bob, ",
          "a well-known couple in Cryptography")
    print("Overview of all the steps:")
    print(_p_green("Alice"), "will")
    print("  generate her private key", _p_blue("(a)"))
    print("  generate public prime number", _p_blue("(p)"))
    print("  calculate base key", _p_blue("(g)"),
          "as a primitive root modulo of", _p_blue("(p)"))
    print("  calculate her public key", _p_blue("(A)"),
          "using the following formula:", _p_yellow("(g)^(a) MOD (p)"))
    print("  share", _p_blue("(g), (p)"), "and her public key",
          _p_blue("(A)"), "with", _p_green("Bob"))
    print(_p_green("Bob"), "will")
    print("  generate his private key", _p_blue("(b)"))
    print("  calculate his public key", _p_blue("(B)"),
          "using the following formula:", _p_yellow("(g)^(b) MOD (p)"))
    print("  share his public key", _p_blue("(B)"), "with", _p_green("Alice"))
    print(_p_green("Alice and Bob"), "will use")
    print("   their private key", _p_blue("(a or b)"), "; and")
    print("   each others public key", _p_blue("(A or B)"), "; and")
    print("   the shared public prime number", _p_blue("(p)"))
    print("   to calculate their shared secret key", _p_blue("(k)"),
          "using the following formula:",
          _p_yellow("(a or b)^(A or B) MOD (p)"))
    _is_done()

    print("It should be obvious that the longer the keys, ",
          "the harder the challenge to either calculate ",
          "(or break) Diffie Hellman.")
    print("This program will challenge you to a competition ",
          "in finding the shared secret", _p_blue("(k)"), "of",
          _p_green("Alice and Bob"))
    print("The program will therefore")
    print("  generate random", _p_blue("a,b and p"), "; and")
    print("  calculate", _p_blue("g,A,B and k"))
    print("")
    print("Let's agree a bit size (>3) for the random generated keys")
    print(Fore.WHITE + "")
    key_length = _input_int("What bit size are you going to try and break: ")
    if key_length < 4:
        raise SystemExit()
    print("")
    print(_p_yellow("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"))
    print("Hint: In decimals, the generated keys")
    print("and prime number will be")
    print("  bigger than", (pow(2, key_length - 1)))
    print("  smaller than", (pow(2, key_length) - 1))
    print(_p_yellow("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"))
    _is_done()

    print(_p_green("Alice"))
    print("  generates public prime key", _p_blue("(p)"),
          "and public base key", _p_blue("(g)"), "...")
    pub_base_key = -1
    while pub_base_key < 0:
        pub_prime_key = _rand_prime(key_length)
        pub_base_key = _find_primitive_root(pub_prime_key)
    print("    done")
    print(_p_green("Alice and Bob"))
    print("  both generate their secret key", _p_blue("(a, b)"), "... ")
    priv_a = _rand_n(key_length)
    priv_b = priv_a
    while priv_a == priv_b:
        priv_b = _rand_n(key_length)
    print("    done")
    print("  and keep them secret, even from Mallory in this program ",
          "(honest! check my source code :P)")
    _is_done()

    print(_p_green("Alice"))
    print("  shares with", _p_green("Bob"), "public base key",
          _p_blue("(g)"), ":",
          _p_blue(str(pub_base_key)), "and public prime number",
          _p_blue("(p)"), ":",
          _p_blue(str(pub_prime_key)), "...")
    _is_done()

    print(_p_green("Alice and Bob"))
    print("  use their private keys", _p_blue("(a, b)"), ";and")
    print("  the public prime number", _p_blue("(p)"), ":",
          _p_blue(str(pub_prime_key)))
    print("  the public base number", _p_blue("(g)"), ":",
          _p_blue(str(pub_base_key)))
    print("  to calculate their public key", _p_blue("(A, B)"), "...", end="")
    thr_pub_a = ThreadWithReturnValue(target=_calc_key,
                                      args=(priv_a, pub_base_key,
                                            pub_prime_key,))
    thr_pub_a.start()
    thr_pub_b = ThreadWithReturnValue(target=_calc_key,
                                      args=(priv_b, pub_base_key,
                                            pub_prime_key,))
    thr_pub_b.start()
    pub_a = thr_pub_a.join()
    pub_b = thr_pub_b.join()
    print("    done")

    print("  exchange their public keys", _p_blue("(A, B)"), ":",
          _p_blue(str(pub_a)), "and", _p_blue(str(pub_b)))
    print("  Alice uses Bob's public key", _p_blue("(B)"), ":",
          _p_blue(str(pub_b)),
          "to calculate their shared secret", _p_blue("(k)"), "...")
    thr_k_a = ThreadWithReturnValue(target=_calc_key,
                                    args=(priv_a, pub_b, pub_prime_key,))
    thr_k_a.start()
    print("  Bob uses Alice's public key", _p_blue("(A)"), ":",
          _p_blue(str(pub_a)),
          "to calculate their shared secret", _p_blue("(k)"), "...")
    thr_k_b = ThreadWithReturnValue(target=_calc_key,
                                    args=(priv_b, pub_a, pub_prime_key,))
    thr_k_b.start()
    k_a = thr_k_a.join()
    k_b = thr_k_b.join()
    _is_done()

    print("Trusted Computer")
    print("  Checks if Alice and Bob have indeed the same shared secret",
          _p_blue("(k)"), "...")
    if k_a != k_b:
        print("   ", _p_red("ERROR"), ": shared secret", _p_blue("(k)"),
              "is not the same")
        exit(1)
    else:
        print("   ", _p_green("SUCCES"),
              "Alice and Bob have indeed calculated ",
              "the same secret", _p_blue("(k)"))
    _is_done()

    print("Now comes the time to test Malory, ",
          "a program to try and find Alice and Bob secret keys...")
    print("Regular CPU", _p_magenta("Mallory"),
          "will try to find either")
    print("  ", _p_green("Alice's"), "secret key", _p_blue("(a)"), "; or")
    print("  ", _p_green("Bob's"), "secret key", _p_blue("(b)"), "; or")
    print("  their shared secret", _p_blue("(k)"))
    print("Using")
    print("  the public prime number", _p_blue("(p)"), ":",
          _p_blue(str(pub_prime_key)))
    print("  the public base number", _p_blue("(g)"), ":",
          _p_blue(str(pub_base_key)))
    print("  Alice's public key", _p_blue("(A)"), ":", _p_blue(str(pub_a)))
    print("  Bob's public key", _p_blue("(B)"), ":", _p_blue(str(pub_b)))
    print("Press ENTER to start the challenge")
    _is_done()

    tic = time.perf_counter()
    print(_p_magenta("Mallory"))
    print("  tries to calculate Alice's and Bob's private key",
          _p_blue("(a, b)"),
          "using public known",
          _p_blue("(A), (B), (p) and (g)"),
          "... ")
    mal_priv_key_a, mal_priv_key_b = _find_secret_key(pub_a, pub_b,
                                                      pub_prime_key,
                                                      pub_base_key)
    print("    done")
    print("  calculates the secret key", _p_blue("(k)"), "of ",
          _p_green("Alice and Bob"), "using the derived shared secrets",
          _p_blue("(a,b)"), "and publicly known",
          _p_blue("(A), (B), (p)"), "... ")
    thr_mal_secret_key_a = ThreadWithReturnValue(target=_calc_key,
                                                 args=(mal_priv_key_a, pub_b,
                                                       pub_prime_key,))
    thr_mal_secret_key_a.start()
    thr_mal_secret_key_b = ThreadWithReturnValue(target=_calc_key,
                                                 args=(mal_priv_key_b, pub_a,
                                                       pub_prime_key,))
    thr_mal_secret_key_b.start()
    mal_secret_key_a = thr_mal_secret_key_a.join()
    mal_secret_key_b = thr_mal_secret_key_b.join()
    print("    done")

    toc = time.perf_counter()
    print(f"  used {toc - tic:0.4f} seconds to complete the task")
    print("What did Mallory find?")
    _check_answer("Alice's Private Key", mal_priv_key_a, priv_a)
    _check_answer("Bob's Private Key", mal_priv_key_b, priv_b)
    _check_answer("Alice & Bob shared secret using Alice's private key",
                  mal_secret_key_a, k_a)
    _check_answer("Alice & Bob shared secret using Bob's private key",
                  mal_secret_key_b, k_b)
    print("NOTE: Their might be collisions (duplicate) private keys",
          _p_blue("(a or b)"),
          "but knowing the shared secret would already be a massive gain")


if __name__ == '__main__':
    main()
