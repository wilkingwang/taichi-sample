"""
Count the prime numbers in the range [1, n]
"""
import taichi as ti

ti.init(arch=ti.gpu)

# Check if a positive integer is a prime number
@ti.func
def is_prime(n: int):
    result = True

    for k in range (2, int(n ** 0.5) + 1):
        if n % k == 0:
            result = False
            break

    return result


# Traverses the large between 2 and n
# Count the primes according to the return of is_prime()
@ti.kernel
def count_prime(n: int) -> int:
    count = 0
    for k in range(2, n):
        if is_prime(k):
            count += 1


    return count

print(count_prime(10000000))
