def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_generator(n):
    for num in range(2, n + 1):
        if is_prime(num):
            yield num


for prime in prime_generator(30):
    print(prime)
