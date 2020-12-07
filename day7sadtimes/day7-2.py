#dict structure: value = bag outside, key = bag inside
dictionaryOfSadness = {}
numberBags = 0

def countBags(color):
    try:
        insideBags = dictionaryOfSadness[color]
    except:
        return
    global numberBags
    numberBags += len(insideBags)
    for bag in insideBags:
        countBags(bag)

with open('advent2020/day7sadtimes/day7input.txt', 'r') as file:
    for rule in file:
        splitRule = rule.strip().split('bags contain ')
        color = splitRule[0].replace(' ','')
        contains = []
        containsListNotClean = splitRule[1].split(',')
        for contents in containsListNotClean:
            words = contents.split()
            if(words[0] == 'no'):
                contains = []
            else:
                for i in range(int(words[0])):
                    contains.append(words[1] + words[2])
        for contents in contains:
            try:
                dictionaryOfSadness[color].append(contents) 
            except:
                dictionaryOfSadness[color] = [contents]     
             
countBags('shinygold')
print(numberBags)