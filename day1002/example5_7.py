import math

strFormat = '%-10s%-10s%-10s'

degree = 0

print(strFormat % ("Degree", "Sin", "Cos"))

while degree <= 360:
    print(strFormat % (degree, format(math.sin(math.radians(degree)), ".4f"), format(math.cos(math.radians(degree)), ".4f")))
    degree += 10
