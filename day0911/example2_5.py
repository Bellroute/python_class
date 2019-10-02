def caculateTip(money, rate):
    return money * rate / 100

def caculateTotal(money, rate):
    return money + caculateTip(money, rate)

def main():
    money, rate = input('Enter the subtotal and a gratuity rate : ').split(', ')
    money = float(money)
    rate = float(rate)
    tip = round(caculateTip(money, rate), 2)
    totoal = round(caculateTotal(money, rate), 2)
    print('The gratutiy is ', tip, 'and the total is', totoal)

if __name__ == "__main__":
    main()