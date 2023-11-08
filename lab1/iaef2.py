from labfuncs import (randN, randPrime, findPrimitiveRoot,
                      calcKey, findSecretKey)


def main():

    bitSize = 16

    print("Given the bitSize of", bitSize)
    print("    the Private keys of Alice & Bob will be")
    print("         larger than:", pow(2, bitSize - 1),"and")
    print("        smaller than:", pow(2, bitSize) - 1)

    pubBaseKey = 0
    while (pubBaseKey < 2):
        pubPrimeKey = randPrime(bitSize)
        primitiveRoots, pubBaseKey = findPrimitiveRoot(pubPrimeKey)
    print("    the Public Prime key (p)")
    print("        is set to:", pubPrimeKey)
    print("    the derived Public Base key (g) is")
    print("        selected from:", primitiveRoots)
    print("        and set to:", pubBaseKey)

    privA = randN(bitSize)
    privB = privA
    while (privA == privB):
        privB = randN(bitSize)

    print("The Private key of")
    print("    Alice is:", privA)
    print("      Bob is:", privB)

    pubA = calcKey(privA, pubBaseKey, pubPrimeKey)
    pubB = calcKey(privB, pubBaseKey, pubPrimeKey)

    print("The Public key of")
    print("    Alice is:", pubA)
    print("      Bob is:", pubB)

    sharedSecretA = calcKey(privA, pubB, pubPrimeKey)
    sharedSecretB = calcKey(privB, pubA, pubPrimeKey)

    if (sharedSecretA != sharedSecretB):
        print("ERROR: Alice's & Bob's sharedSecret are not the same")
        exit()

    print("The Shared secret of")
    print("    Alice is:", sharedSecretA)
    print("      Bob is:", sharedSecretB)

    print("Malory determines")
    malPrivKeyA, malPrivKeyB = findSecretKey(pubA, pubB,
                                             pubPrimeKey, pubBaseKey)

    print("    Alice's private key to be:", malPrivKeyA)
    print("    Bob's private key to be:", malPrivKeyB)

    malSharedSecretA = calcKey(malPrivKeyA, pubB, pubPrimeKey)
    malSharedSecretB = calcKey(malPrivKeyB, pubA, pubPrimeKey)

    print("    Alice's shared secret to be:", malSharedSecretA)
    print("    Bob's shared secret to be:", malSharedSecretB)


if __name__ == '__main__':
    main()
