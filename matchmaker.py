import pandas as pd
# import UNSPSC_structure_dict_unsorted as UNSPSC
import UNSPSC_structure_dict as UNSPSC
# import Avalara_structure as Avalara
import Avalara_structure_titles_only_sorted as Avalara
import time

# Global variables
UNSPSC_dict = UNSPSC.getDict()
Avalara_dict = Avalara.Ava_Dict().dict
UNSPSC_data = UNSPSC_dict.data

# Final version -- assumes input word lists are both sorted lexicographically
def sortedMatch():

    print(">> Beginning matching...")
    timerMain = time.time()
    output_dict = {}

    # For every key-value pair in Avalara dict
    for avaKey, avaVal in Avalara_dict.items():
        start = time.time()
        print(">>>> Matching ", avaKey, "...")
        maxCount = 0
        maxCommodityID = -1
        avaTaxID = avaKey
        avaWordList = avaVal

        # Check every UNSPSC item
        for targetKey, targetVal in UNSPSC_data.items():
            currCount = 0
            currCommodityID = targetKey
            currTargetWordList = targetVal
            currTargetIndex = 0
            length = len(currTargetWordList)

            # Iterate through word list of every UNSPSC item. 
            avaIndex = 0
            while currTargetIndex < length and avaIndex < len(avaWordList):
                if len(avaWordList) < 1:
                    break
                while avaIndex < len(avaWordList):
                    while currTargetIndex < length:
                        if avaWordList[avaIndex] == currTargetWordList[currTargetIndex]:
                            currCount += 1
                            currTargetIndex += 1
                            break
                        elif avaWordList[avaIndex] > currTargetWordList[currTargetIndex]:
                            currTargetIndex += 1
                        else:
                            break
                    avaIndex += 1
            if currCount > maxCount:
                maxCount = currCount
                maxCommodityID = currCommodityID
                
        print(avaTaxID, " matched with ", maxCommodityID)
        output_dict[avaTaxID] = [avaWordList, maxCommodityID]
        end = time.time()
        print(f">>>> Match took {round(end - start, 2)} seconds.")

    print(">> Matching ended.")
    timerMainEnd = time.time()
    print(f">> Process took {round(timerMainEnd - timerMain, 2)} seconds.")
    fileHandle = open("proj_output.txt", "a")
    for key, value in output_dict.items():
        fileHandle.write(str(key) + " " + str(value[0]) + " was matched with " + str(value[1]) + '\n')
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
