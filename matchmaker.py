import pandas as pd
import UNSPSC_structure_dict as UNSPSC
import Avalara_structure as Avalara

UNSPSC_dict = UNSPSC.getDict()
Avalara_utility = Avalara.ReadFile()
Avalara_utility.read()
AvalaraDict = Avalara_utility.dict

def main():

    UNSPSC_dict.printHashmap()


if __name__ == "__main__":
    main()
