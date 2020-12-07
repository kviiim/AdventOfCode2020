#dict structure: value = bag inside, key = bag outside
dictionaryOfSadness = {}
possibleBags = []

def findBags(color):
    try:
        outsideBags = dictionaryOfSadness[color]
    except:
        return
    for bag in outsideBags:
        if not bag in possibleBags:
            possibleBags.append(bag)
            findBags(bag)

with open('advent2020/day7sadtimes/day7input.txt', 'r') as file:
    for rule in file:
        splitRule = rule.strip().split('bags contain ')
        color = splitRule[0].replace(' ','')
        contains = []
        containsListNotClean = splitRule[1].split(',')
        for contents in containsListNotClean:
            words = contents.split()
            contains.append(words[1] + words[2])
        if contains[0] == 'otherbags.':
            contains = []
        for contents in contains:
            try:
                dictionaryOfSadness[contents].append(color) 
            except:
                dictionaryOfSadness[contents] = [color]     
             
findBags('shinygold')
print(len(possibleBags))