import numpy as np

with open('advent2020/day12/day12input.txt', 'r') as file:
    directions = [[x.strip()[0], int(x.strip()[1:])] for x in file.readlines()]

theta = 0
x = 0
y = 0

for direction in directions:
    if direction[0] == 'F':
        if theta == 0:
            x += direction[1]
        elif theta == 90:
            y += direction[1]
        elif theta == 180:
            x -= direction[1]
        elif theta == 270:
            y -= direction[1]
    elif direction[0] == 'L':
        theta += direction[1]
        if theta >= 360:
            theta -= 360
        elif theta < 0:
            theta += 360
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

print(x,y, abs(x) + abs(y))