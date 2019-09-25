# Given a number n, print all primes smaller than or equal to n.
# It is also given that n is a small number.
# The sieve of Eratosthenes is one of the most efficient ways to find all primes smaller
# than n when n is smaller than 10 million or so

def SieveOfEratosthenes(n):
    if n < 0:
        return
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p] is True:
            for j in range(p * p, n + 1, p):
                prime[j] = False
        p += 1
    for p in range(2, n):
        if prime[p]:
            print(p, end=" ")


if __name__ == '__main__':
    n = 30
    print("Following are the numbers smaller than equal to n:")
    SieveOfEratosthenes(n)
