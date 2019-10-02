import prime

def factorize(n):
    factor = []
    
    while True:
        m = prime.isPrime(n)
        if m == n:
            break
        n //= m
    return factor

def main():
    n = int(input('type any number : '))
    result = prime.isPrime(n)
    if result:
        print(n, '은 소수야!')
    else:
        print(n, '은 ', result, '로 나눠져!')

    result = factorize(n)
    print(result)


if __name__ == "__main__":
    main()
        