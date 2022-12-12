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

                        # If Avalara word lexicographically greater, then check next UNSPSC word for match
                        elif avaWordList[avaIndex] > currTargetWordList[currTargetIndex]:
                            currTargetIndex += 1

                        # If Avalara word lexicographically smaller, then check next Avalara word
                        else:
                            break

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


# Deprecated -- Rabin Karp hashing algorithm for matching a word (pattern) to a string (text)
def rabinKarp(pattern, text):

    d = 26 # a b c ... z
    q = 5381 # large prime number
    m = len(pattern)
    n = len(text)
    p = 0 # hash for pattern
    t = 0 # hash for text
    h = 1
    i = 0
    j = 0
        
    res = []
        
    for i in range(m-1):
        h = (h*d) % q
        
    for i in range(m):
        p = (d*p + ord(pattern[i])) % q
        t = (d*t + ord(text[i])) % q
        
    for i in range(n-m+1):
        if p == t:
            for j in range(m):
                if text[i+j] != pattern[j]:
                    break
            j += 1
            if j == m:
                res.append(i)
            
        if i < n-m:
            t = (d*(t-ord(text[i])*h) + ord(text[i+m])) % q
                
            if t < 0:
                t = t + q
                    
    return res


# Deprecated
def rabinKarpMatch():

    # UNSPSC_dict.printDict()
    print("matching begins......")
    output_dict = {}
    for k_ava, v_ava in Avalara_dict.items():
        start = time.time()
        print(k_ava)
        maxCount = 0
        commodityID = -1
        taxID = k_ava
        taxWordList = v_ava
        for k_UN, v_UN in UNSPSC_data.items():
            currCount = 0
            currcommodityID = k_UN
            strData = v_UN
            # print(currcommodityID)
            for word in taxWordList:
                currCount += len(rabinKarp(word, strData))
            if currCount > maxCount:
                maxCount = currCount
                commodityID = currcommodityID
        
        output_dict[taxID] = commodityID
        end = time.time()
        print(f"one matching takes {round(end - start, 2)} secs")
        print(f"max count is {maxCount}")

    print("matching ends......")
    fileHandle = open("proj_output.txt", "a")

    for k, v in output_dict.items():
        fileHandle.write(str(k) + "is matching with " + str(v) + '\n')
    fileHandle.close()

def main():
    sortedMatch()

if __name__ == "__main__":
    main()
