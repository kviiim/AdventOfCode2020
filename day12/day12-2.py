import numpy as np

with open('advent2020/day12/day12input.txt', 'r') as file:
    directions = [[x.strip()[0], int(x.strip()[1:])] for x in file.readlines()]

shipX = 0
shipY = 0
#x and y are relative to the ship
x = 10
y = 1

for direction in directions:
    if direction[0] == 'F':
        shipX += x*direction[1]
        shipY += y*direction[1]
    elif direction[0] == 'L' or direction[0] == 'R':
        if direction[0] == 'R':
            angle = 360 - direction[1]
        else:
            angle = direction[1]
        if angle == 90:
            newx = -y
            newy = x
            x = newx
            y = newy
        elif angle == 180:
            x = -x
            y = -y
        if angle == 270:
            newx = y
            newy = -x
            x = newx
            y = newy
    elif direction[0] == 'R':
        theta -= direction[1]
        if theta >= 360:
            theta -= 360
        elif theta < 0:
            theta += 360
    elif direction[0] == 'N':
        y += direction[1]
    elif direction[0] == 'S':
        y -= direction[1]
    elif direction[0] == 'E':
        x += direction[1]
    elif direction[0] == 'W':
        x -= direction[1]
print(abs(shipX) + abs(shipY))