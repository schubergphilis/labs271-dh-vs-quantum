import sys

# translated to Python from http://www.bluetulip.org/2014/programs/primitive.js
# (some rights may remain with the author of the above javascript code)

def isNotPrime(possible):
    # We only test this here to protect people who copy and paste
    # the code without reading the first sentence of the answer.
    # In an application where you know the numbers are prime you
    # will remove this function (and the call). If you need to
    # test for primality, look for a more efficient algorithm, see
    # for example Joseph F's answer on this page.
    i = 2
    while i*i <= possible:
        if (possible % i) == 0:
            return True
        i = i + 1
    return False

def primRoots(theNum):
    if isNotPrime(theNum):
        raise ValueError("Sorry, the number must be prime.")
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
    return roots

print(primRoots(int(sys.argv[1])))