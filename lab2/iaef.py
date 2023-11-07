import random
from math import gcd
from braket.devices import LocalSimulator
from braket.aws import AwsDevice
from braket.experimental.algorithms.shors.shors import (
    shors_algorithm,
    run_shors_algorithm,
    get_factors_from_results
)


def randN(bits: int):
    # bits to decimal
    min = pow(2, bits-1)
    max = pow(2, bits) - 1
    result = random.randint(min, max)
    print("N is set to:", result)
    return result


def main():
    # Main function

    nrOfBits = 6
    N = randN(nrOfBits)

    a = 2
    result = []
    while 1 < a < N:
        if (gcd(a, N) == 1):
          result.append(a)
    a = random.choice(result)

    shors_circuit = shors_algorithm(N, a)
    local_simulator = LocalSimulator()
    output = run_shors_algorithm(shors_circuit, local_simulator)
    guessed_factors = get_factors_from_results(output, N, a)
    print(guessed_factors)


if __name__ == '__main__':
    main()
