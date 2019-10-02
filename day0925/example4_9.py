weight1, price1 = input('Enter weight and price for package 1: ').split(', ')
weight2, price2 = input('Enter weight and price for package 2: ').split(', ')

costPerWeight1 = float(price1) / int(weight1)
costPerWeight2 = float(price2) / int(weight2)

if costPerWeight1 < costPerWeight2:
    print('Package 2 has the better price.')
elif costPerWeight1 > costPerWeight2:
    print('Package 1 has the better price.')
else:
    print('same same')