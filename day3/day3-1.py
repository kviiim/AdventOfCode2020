treeArray = []
with open('advent2020/day3/day3input.txt', 'r') as file:
    for line in file.readlines():
        treeArray.append(line.strip("\n"))

horizontalDeltaIndexList = [1, 3, 5, 7, 1]
verticalDeltaIndexList = [1, 1, 1, 1, 2]
treesMultiplied = 1

for pathNum in range(len(horizontalDeltaIndexList)):
    numTrees = 0
    horizontalIndex = 0
    verticalIndex = 0
    maxIndex = len(treeArray[0]) - 1
    while verticalIndex < len(treeArray):
        line = treeArray[verticalIndex]
        if line[horizontalIndex] == "#":
            numTrees += 1
        if horizontalIndex + horizontalDeltaIndexList[pathNum] > maxIndex:
            horizontalIndex = (horizontalDeltaIndexList[pathNum] - 1) - (maxIndex - horizontalIndex)
        else:
            horizontalIndex += horizontalDeltaIndexList[pathNum]
        verticalIndex += verticalDeltaIndexList[pathNum]
    treesMultiplied *= numTrees
print(treesMultiplied)
