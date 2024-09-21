from sympy.ntheory import isprime

maxLimit = 10000

for n in range(maxLimit+1):
    print(isprime(n))
