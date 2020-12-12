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

def run_sim(layout):
    newLayout = copy.deepcopy(layout)
    for row in range(len(layout)):
        for col in range(len(layout[row])):
            curVal = layout[row][col]
            if (curVal == 'L' or curVal == '#'):
                surrounding = [
                layout[row + 1][col],
                layout[row - 1][col],
                layout[row][col + 1],
                layout[row][col - 1],
                layout[row + 1][col + 1],
                layout[row + 1][col - 1],
                layout[row - 1][col + 1],
                layout[row - 1][col - 1]]

                if curVal == 'L' and surrounding.count('#') == 0:
                    newLayout[row][col] = '#'
                elif curVal == '#' and surrounding.count('#') >= 4:
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

                
                