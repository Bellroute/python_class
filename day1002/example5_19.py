inputValue = int(input("Enter the number of lines: "))

for i in range(1, inputValue + 1):
    line = " "
    for j in range(i, 0, -1):
        line += str(j) + " "

    for j in range(2, i + 1):
        line += str(j) + " "

    print(line.center(60))
