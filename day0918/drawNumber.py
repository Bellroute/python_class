import random

def inputBoundary():
    return int(input('몇 번까지 추첨할지 입력 : '))

def inputCount():
    return int(input('추첨 횟수 입력 : '))

def do(boundary, count):

    shuffledList = shuffle(boundary)

    return shuffledList[0:count]

def shuffle(boundary):
    list = []

    for i in range(1, boundary + 1):
        list.append(i)

    random.shuffle(list)

    return list



def main():
    boundary = inputBoundary()
    count = inputCount()

    print('추첨 번호는', do(boundary, count), '입니다')


if __name__ == "__main__":
    main()