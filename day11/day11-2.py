import copy
ogLayout = []
with open('advent2020/day11/day11input.txt', 'r') as file:
    for line in file:
        row = list(line.strip())
        row.insert(0, 'e')
        row.append('e')
        ogLayout.append(row)

ogLayout.insert(0, ['e' for i in range(len(ogLayout[0]))])
ogLayout.append(['e' for i in range(len(ogLayout[0]))])

slopes = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]

print(ogLayout)
print(len(ogLayout), len(ogLayout[0]))

def run_sim(layout):
    newLayout = copy.deepcopy(layout)
    for row in range(len(layout)):
        for col in range(len(layout[row])):
            curVal = layout[row][col]
            if curVal != 'e':
                surrounding = []
                for slope in slopes:
                    curCheckVal = '.'
                    curCheckCoords = [row, col]
                    while (curCheckVal == '.'):
                        curCheckCoords = [curCheckCoords[0] + slope[0], curCheckCoords[1] + slope[1]]
                        curCheckVal = layout[curCheckCoords[0]][curCheckCoords[1]]
                    if curCheckVal != 'e':
                        surrounding.append(curCheckVal)
                if curVal == 'L' and surrounding.count('#') == 0:
                    newLayout[row][col] = '#'
                elif curVal == '#' and surrounding.count('#') >= 5:
                    newLayout[row][col] = 'L'
    if (newLayout == layout):
        totalOcc = 0
        for row in layout:
            totalOcc += (row.count('#'))
        print(totalOcc, 'seats occupied')
        return
    else:
        return run_sim(newLayout)

run_sim(ogLayout)

                
                