def get_prime_factors(input):
    factors = []
    for n in range(2, input+1):
        if input == 1:
            factors = []
        elif input % n == 0:  # check if n is divisor of input
            factors.append(n)
            factors = factors + get_prime_factors(int(input / n))
            break
    return factors


while (True):
    num = int(input("enter a number: "))
    print(get_prime_factors(num))
