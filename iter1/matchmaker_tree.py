import Avalara_structure
import UNSPSC_structure_tree as UNSPSC_structure
import time

UNSPSC_tree = UNSPSC_structure_tree.getTree()
Avalara_utility = Avalara_structure.Ava_Dict()
Avalara_utility.read()
AvalaraDict, matchSolution = Avalara_utility.dict, Avalara_utility.solution

def matchAll():

    numOfMatches = 0

    print('>> Beginning matching...')
    start = time.time()

    for key in AvalaraDict:
        wordList = AvalaraDict[key]
        iter = UNSPSC_tree
        maxCount = 0
        while not isinstance(iter, UNSPSC_structure.UNSPSC_Commodity):
            maxCount = 0
            childIndex = -1
            maxChildIndex = float('inf')
            for child in iter.childList:
                childIndex += 1
                currCount = 0
                comparatorList = child.definition
                comparatorList.append(child.title)
                for word in wordList:
                    for comparator in comparatorList:
                        if word == comparator:
                            currCount += 1
                if currCount > maxCount:
                    maxCount = currCount
                    maxChildIndex = childIndex
            if maxCount == 0:
                break
            else:
                iter = iter.childList[maxChildIndex]
        if maxCount > 0:
            matchSolution.resultsDict[key].extend([iter.key, iter.id, iter.title])
            numOfMatches += 1

    print('>>>> Matching complete. Process took %s seconds.\n' % (round((time.time() - start), 2)))
    print('>>>> %d matches made.\n' % numOfMatches)

def main():

    matchAll()
    matchSolution.writeToFile()


if __name__ == "__main__":
    main()