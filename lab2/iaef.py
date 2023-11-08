import random
from math import gcd
from braket.devices import LocalSimulator
from braket.aws import AwsDevice
from braket.experimental.algorithms.shors.shors import (
    shors_algorithm,
    run_shors_algorithm,
    get_factors_from_results
)


def _inputInt(message, input_type=int):
    while True:
        try:
            return input_type(input(message))
        except TypeError:
            print("Type error: '{0}'.".format(message))
            exit(1)
        except Exception as e:
            print("Error '{0}' occurred. Arguments {1}.".format(e.message,
                                                                e.args))
            exit(1)


def randN(bits: int):
    # bits to decimal
    min = pow(2, bits-1)
    max = pow(2, bits) - 1
    result = random.randint(min, max)
    print("N is set to:", result)
    return result


def main():
    # Main function

    nrOfBits = _inputInt(
        "What bit size are you going to try and break: ", int)

    N = randN(nrOfBits)

    a = 2
    result = []
    while 1 < a < N:
        if (gcd(a, N) == 1):
            print("Found an eligible a:", a)
            result.append(a)
        a += 1
    a = random.choice(result)
    print("a is set to:", a)

    print("Defining circuit")
    shors_circuit = shors_algorithm(N, a)

    print("Setting up the simulator")
    local_simulator = LocalSimulator()

    print("Run the algorithm")
    output = run_shors_algorithm(shors_circuit, local_simulator)

    guessed_factors = get_factors_from_results(output, N, a)
    print(guessed_factors)


if __name__ == '__main__':
    main()
