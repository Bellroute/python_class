inputList = []
positives = 0
negatives = 0
total = 0


while True:
    num = eval(input("Enter an integer, the input ends if it is 0: "))

    if num == 0:
        break
    
    inputList.append(num)

for i in range(len(inputList)):
    if inputList[i] % 2 == 0:
        negatives += 1
    else:
        positives += 1

    total += inputList[i]

average = total / len(inputList)

print("The number of positives is ", positives)
print("The number of negatives is ", negatives)
print("The total is ", total)
print("The average is ", average)