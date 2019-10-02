def main():
    x = int(input('type a starting number : '))
    y = int(input('type an ending number : '))

    sumx = 0
    for i in  range(x, y+1):
        if i % 2 == 0:
            sumx += 1

    print(sumx)

if __name__ == '__main__':
    main()