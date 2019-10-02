n1, n2, n3 = input("정수 3개를 입력: ").split(' ')

a = [n1, n2, n3]
temp = 0
for i in range(0,3):
    for j in range(i+1,3):
        if a[i] > a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp

for i in range(3):
    print(a[i])