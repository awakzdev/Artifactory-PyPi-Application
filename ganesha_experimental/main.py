import random


def isPrime(n):
    # Corner case
    if n <= 1:
        return False

    # check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False

    return True


# Function to print primes
def printPrime(n):
    previous_primes_nb = []
    for i in range(2, n + 1):
        if isPrime(i):
            previous_primes_nb.append(i)
    return previous_primes_nb


def Prime():
    n = random.randint(2, 100)
    Prime = str(printPrime(n))[1:-1]
    print(Prime)



if __name__ == "__main__":
    Prime()

