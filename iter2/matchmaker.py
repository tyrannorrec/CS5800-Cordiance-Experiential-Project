import pandas as pd
import UNSPSC_structure_dict_unsorted as UNSPSC
# import Avalara_structure as Avalara
import Avalara_structure_titlesonly as Avalara
import time

# Global variables
UNSPSC_dict = UNSPSC.getDict()
UNSPSC_data = UNSPSC_dict.data
Avalara_dict = Avalara.Ava_Dict()
Avalara_data = Avalara_dict.data

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

    print("matching begins......")
    output_dict = {}
    for k_ava, v_ava in Avalara_data.items():
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
    rabinKarpMatch()

if __name__ == "__main__":
    main()
