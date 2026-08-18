import datetime
import time

def simple_prime_search(n):
    primes = []
    for num in range(2, n+1):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
        if is_prime:
            primes.append(num)
    return primes


def sieve_eratosthenes(n):
    sieve = [True] * (n + 1)
    sieve[0] = False
    sieve[1] = False
    for p in range(2, int(n**0.5)+1):
        if sieve[p]:
            for i in range(p*p, n+1, p):
                sieve[i] = False
    return [p for p, is_prime in enumerate(sieve) if is_prime]

def measure_time(func, *args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    print(f"Time of the function {func.__name__}: {end - start:.10f} seconds")
    return result

limits = [100,1000, 10000]

for limit in limits:
    print(f"Діапазон --- {limit}")

    print("Simple_search:")
    measure_time(simple_prime_search, limit)

    print("Sieve_eratosthenes:")
    measure_time(sieve_eratosthenes, limit)
