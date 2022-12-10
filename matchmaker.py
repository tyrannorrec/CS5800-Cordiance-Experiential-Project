import pandas as pd
import UNSPSC_structure_dict as UNSPSC
# import Avalara_structure as Avalara
import Avalara_structure_titles_only_sorted as Avalara

import Rabin_Karp_match as RK
import time


UNSPSC_dict = UNSPSC.getDict()
Avalara_utility = Avalara.ReadFile()
Avalara_utility.read()
AvalaraDict = Avalara_utility.dict

def main():
    sortedMatch()

if __name__ == "__main__":
    main()
