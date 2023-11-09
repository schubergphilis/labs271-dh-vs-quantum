    from argparse import ArgumentParser


def calc_shared_key(a, b, p, g):
    a_, b_ = None, None
    for x in range(1, p):
        if (g ** x) % p == a:
            a_ = x
        if (g ** x) % p == b:
            b_ = x
    return a_, b_


def main():
    parser = ArgumentParser()
    parser.add_argument("-A", "--A_public_key", required=True)
    parser.add_argument("-B", "--B_public_key", required=True)
    parser.add_argument("-g", "--base", required=True)
    parser.add_argument("-p", "--prime", required=True)
    args = parser.parse_args()

    a = int(args.alice)
    b = int(args.bob)
    g = int(args.base)
    p = int(args.prime)

    a_, b_ = calc_shared_key(a, b, p, g)
    
    if a_ is not None:
        print('A private key is {}'.format(a_))
    else:
        print("Could not find the A's private key :(")

    if b_ is not None:
        print('B private key is {}'.format(b_))
    else:
        print("Could not find the B's private key :(")

    if a_ is not None and b_ is not None:
        k = (b ** a_) % p
        print('A and B shared secret key is {}'.format(k))
    else:
        print('Could not find the shared key :(')


if __name__ == '__main__':
    main()