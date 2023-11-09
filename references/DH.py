from argparse import ArgumentParser


def calc_key(key, g, p):
    return (g ** key) % p


def main():
    parser = ArgumentParser()
    parser.add_argument("-A", "--A_private_key", required=True)
    parser.add_argument("-B", "--B_private_key", required=True)
    parser.add_argument("-g", "--base", required=True)
    parser.add_argument("-p", "--prime", required=True)
    args = parser.parse_args()

    a = int(args.a_private_key)
    b = int(args.b_private_key)
    g = int(args.base)
    p = int(args.prime)

    a_public_key = calc_key(a, g, p)
    b_public_key = calc_key(b, g, p)

    a_shared_key = calc_key(a, b_public_key, p)
    b_shared_key = calc_key(b, a_public_key, p)

    print('Shared secret: {}'.format(a_shared_key))



if __name__ == '__main__':
    main()