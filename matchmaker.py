import pandas as pd
import UNSPSC_structure_dict as UNSPSC
# import Avalara_structure as Avalara
import Avalara_structure_only_2nd_column as Avalara
import Rabin_Karp_match as RK
import time


UNSPSC_dict = UNSPSC.getDict()
Avalara_dict = Avalara.Ava_dict().dict

UNSPSC_data = UNSPSC_dict.data

def main():

    # UNSPSC_dict.printDict()
    print("matching begins......")
    rabinKarp = RK.string_to_int()
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
                currCount += len(rabinKarp.rabin_karp_helper(word, strData))
            if currCount > maxCount:
                maxCount = currCount
                commodityID = currcommodityID
        
        output_dict[taxID] = commodityID
        end = time.time()
        print(f"one matching takes {round(end - start, 2)} secs")
        print(f"max count is {maxCount}")

    print("matching ends......")
    f = open("proj_output.txt", "a")

    for k, v in output_dict.items():
        f.write(str(k) + "is matching with " + str(v) + '\n')
    f.close()

if __name__ == "__main__":
    main()
