sum = 0.0
for i in range(1, 50):
    son = 2 * i - 1
    mom = 2 * i + 1

    sum += son / mom

print(sum)