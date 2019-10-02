def isPrime(n):

    for i in range(2, n):

        if n % i == 0:
            return False
    return True

def main():
    inputNumber = int(input('input a number for checking : '))
    
    if isPrime(inputNumber) :
        print('yes')
    else: 
        return print('no')

if __name__ == '__main__':
    main()