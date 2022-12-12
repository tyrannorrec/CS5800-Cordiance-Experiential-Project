import pandas as pd
# import UNSPSC_structure_dict_unsorted as UNSPSC
import iter4.UNSPSC_structure_dict as UNSPSC
# import Avalara_structure as Avalara
import Avalara_structure_titles_only_sorted as Avalara
import time

# Global variables
UNSPSC_dict = UNSPSC.getDict()
UNSPSC_data = UNSPSC_dict.data
Avalara_dict = Avalara.Ava_Dict()
Avalara_data = Avalara_dict.data
# res = Avalara_dict.results

# Final version -- assumes input word lists are both sorted lexicographically
def sortedMatch():

    print(">> Beginning matching...")
    startAll = time.time()
    output_dict = {}

    # For every key-value pair in Avalara dict
    for avaKey, avaVal in Avalara_data.items():
        startMatch = time.time()
        print(">>>> Matching ", avaKey, "...")
        maxCount = 0
        maxCommodityID = -1
        avaTaxID = avaKey
        avaWordList = avaVal

        # For every item in UNSPSC dictionary
        for targetKey, targetVal in UNSPSC_data.items():
            currCount = 0
            currCommodityID = targetKey
            currTargetWordList = targetVal
            currTargetIndex = 0
            length = len(currTargetWordList)
            avaIndex = 0

            # While either Avalara or UNSPSC word list has not been exhausted
            while currTargetIndex < length and avaIndex < len(avaWordList):

                # Edge case where list is empty
                if len(avaWordList) < 1:
                    break

                # For every word in Avalara word list
                while avaIndex < len(avaWordList):

                    # Check every word in UNSPSC word list
                    while currTargetIndex < length:

                        # If there is a match, increment count, go to next UNSPSC word and next Avalara word
                        if avaWordList[avaIndex] == currTargetWordList[currTargetIndex]:
                            currCount += 1
                            currTargetIndex += 1
                            break

                        # If Avalara word lexicographically smaller or larger, then check next UNSPSC word
                        else:
                            currTargetIndex += 1

                    avaIndex += 1

            # Update to best match if appropriate
            if currCount > maxCount:
                maxCount = currCount
                maxCommodityID = currCommodityID
    
        output_dict[avaTaxID] = [avaWordList, maxCommodityID]
        #res.at[avaKey, 'Commodity ID'] = maxCommodityID

        print(avaTaxID, " matched with ", maxCommodityID)
        print(f">>>> Match took {round(time.time() - startMatch, 2)} seconds.")

    print(">> Matching ended.")
    print(f">> Process took {round(time.time() - startAll, 2)} seconds.")

    # Write results to output file
    fileHandle = open("proj_output.txt", "a")
    for key, value in output_dict.items():
        fileHandle.write(str(key) + " " + str(value[0]) + " was matched with " + str(value[1]) + '\n')
    #fileHandle.write(res.to_string())
    fileHandle.close()

def main():
    sortedMatch()

if __name__ == "__main__":
    main()
