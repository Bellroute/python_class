def changeToFahrenheit(celsius):
    return (9 / 5) * celsius + 32

def main():
    celsius = int(input('섭씨로 온도를 입력하세요: '))
    fahrenheit = changeToFahrenheit(celsius)
    print('섭씨', celsius, '도는 화씨 ', fahrenheit, '도 입니다.')

if __name__ == "__main__":
    main()