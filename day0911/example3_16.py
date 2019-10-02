import math
import turtle

def calculateArea(l1, l2, l3):
    s = (l1 + l2 + l3) / 2
    area = s * (s - l1) * (s - l2) * (s - l3)
    area = math.sqrt(area)

    return area

def calculatelength(x1, y1, x2, y2):
    return math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))

def drawTriangle(x1, y1, x2, y2, x3, y3, area):
    turtle.pensize(3)
    turtle.penup()
    turtle.goto(min(x1, x2, x3), min(y1, y2, y3) - 20)
    turtle.pendown()
    turtle.write('삼각형의 면적은', area)
    turtle.hidetutle()

def main():
    p1_x, p1_y, p2_x, p2_y, p3_x, p3_y = input('Enter three points : ').split(', ')
    p1_x = float(p1_x)
    p1_y = float(p1_y)
    p2_x = float(p2_x)
    p2_y = float(p2_y)
    p3_x = float(p3_x)
    p3_y = float(p3_y)

    l1 = calculatelength(p1_x, p1_y, p2_x, p2_y)
    l2 = calculatelength(p2_x, p2_y, p3_x, p3_y)
    l3 = calculatelength(p3_x, p3_y, p1_x, p2_y)

    result = calculateArea(l1, l2, l3)
    drawTriangle(p1_x, p1_y, p2_x, p2_y, p3_x, p3_y, result)

if __name__ == "__main__":
    main()