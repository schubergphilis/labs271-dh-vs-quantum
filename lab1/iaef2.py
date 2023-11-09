from labfuncs import (rand_n, rand_prime, find_primitive_root,
                      calc_key, find_secret_key)


def main():
    bit_size = 16

    print("Given the bitSize of", bit_size)
    print("    the Private keys of Alice & Bob will be")
    print("         larger than:", pow(2, bit_size - 1), "and")
    print("        smaller than:", pow(2, bit_size) - 1)

    pub_base_key = 0
    pub_prime_key = None
    primitive_roots = None
    while pub_base_key < 2:
        pub_prime_key = rand_prime(bit_size)
        primitive_roots, pub_base_key = find_primitive_root(pub_prime_key)
    print("    the Public Prime key (p)")
    print("        is set to:", pub_prime_key)
    print("    the derived Public Base key (g) is")
    print("        selected from:", primitive_roots)
    print("        and set to:", pub_base_key)

    priv_a = rand_n(bit_size)
    priv_b = priv_a
    while priv_a == priv_b:
        priv_b = rand_n(bit_size)

    print("The Private key of")
    print("    Alice is:", priv_a)
    print("      Bob is:", priv_b)

    pub_a = calc_key(priv_a, pub_base_key, pub_prime_key)
    pub_b = calc_key(priv_b, pub_base_key, pub_prime_key)

    print("The Public key of")
    print("    Alice is:", pub_a)
    print("      Bob is:", pub_b)

    shared_secret_a = calc_key(priv_a, pub_b, pub_prime_key)
    shared_secret_b = calc_key(priv_b, pub_a, pub_prime_key)

    if shared_secret_a != shared_secret_b:
        print("ERROR: Alice's & Bob's sharedSecret are not the same")
        exit()

    print("The Shared secret of")
    print("    Alice is:", shared_secret_a)
    print("      Bob is:", shared_secret_b)

    print("Malory determines")
    mal_priv_key_a, mal_priv_key_b = find_secret_key(pub_a, pub_b,
                                                     pub_prime_key, pub_base_key)

    print("    Alice's private key to be:", mal_priv_key_a)
    print("    Bob's private key to be:", mal_priv_key_b)

    mal_shared_secret_a = calc_key(mal_priv_key_a, pub_b, pub_prime_key)
    mal_shared_secret_b = calc_key(mal_priv_key_b, pub_a, pub_prime_key)

    print("    Alice's shared secret to be:", mal_shared_secret_a)
    print("    Bob's shared secret to be:", mal_shared_secret_b)


if __name__ == '__main__':
    main()
