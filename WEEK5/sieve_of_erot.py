primes = []
numbers = [1 for _ in range(2, 1000)]


# for i in range(4, 1000, 2):
#     primes.append(i)
# print(primes)

# print(primes)

def Sieve(num=1000):
    '''This function return a prime numbers for a parameter provided'''
    numbers = []
    prime = [1 for _ in range(num + 1)]
    p = 2
    while p <= num:
        if prime[p] == 1:
            for i in range(p * p, num + 1, p):
                prime[i] = 0
        p += 1
    # print(prime)
    for p in range(2, num + 1):
        print(prime[p])
        if prime[p]:
            numbers.append(p)
    print(numbers)


Sieve()
print(Sieve.__doc__)
