import pandas as pd
import time
import re
import math


class UNSPSC_Dict:

    def __init__(self, inDataFrame):

        self.df = inDataFrame
        self.data = {}

        print('>> Building UNSPSC dictionary...')
        start = time.time()
        self.build()
        print('>>>> Build complete. Process took %s seconds.\n' % (round((time.time() - start), 2)))

    # Parses data frame and builds hashmap. Called by initializer.
    def build(self):

        # Checks for empty str and returns str in lower caps.
        def lowerStr(inStr):

            if isinstance(inStr, str) and len(inStr) > 0:
                return inStr.lower()
            else:
                return ''

        # Sorts string as list of words and returns as string.
        def sortStringLex(inStr):
            #strDataList = inStr.split()
            strDataList = [*set(inStr)] # Removes duplicates
            strDataList.sort()
            return strDataList

        # Extracts all text elements for item in UNSPSC file and outputs a string representing that item for hashing
        def getStringData(i):
            
            strData = ''
            strData = (strData + lowerStr(self.df['Segment Title'][i]) + ' ' + lowerStr(self.df['Segment Definition'][i]) + ' ' + 
                            lowerStr(self.df['Family Title'][i]) + ' ' + lowerStr(self.df['Family Definition'][i]) + ' ' + 
                            lowerStr(self.df['Class Title'][i]) + ' ' + lowerStr(self.df['Class Definition'][i]) + ' ' +
                            lowerStr(self.df['Commodity Title'][i]) + ' ' + lowerStr(self.df['Definition'][i]))
            #strData = (strData + lowerStr(self.df['Segment Title'][i]) + ' ' + 
            #                lowerStr(self.df['Family Title'][i]) + ' ' + 
            #                lowerStr(self.df['Class Title'][i]) + ' ' +
            #                lowerStr(self.df['Commodity Title'][i]))
 
            strData = re.findall(r'\w+', strData)
            for word in strData:
                if len(word) <= 3:
                    strData.remove(word)
            return sortStringLex(strData)

        # For each item in UNSPSC file, add item to dictionary where key = commodity ID and value = hash string for item
        for i in self.df.index:
            commodityID = self.df['Commodity'][i]
            if not math.isnan(commodityID):
                strData = getStringData(i)
                self.data[int(commodityID)] = strData

    def printDict(self):

        for key in self.data:
            print(key, '\t', self.data[key], '\n')


def getDict():

    print('\n>> Converting UNSPSC file to data frame...')
    start = time.time()
    UNSPSC_df = pd.read_excel('UNSPSC_English_excel.xlsx', 'UNSPSC_English_excel', usecols=[0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14], skiprows=9)
    print('>>>> Conversion complete. Process took %s seconds.\n' % (round((time.time() - start), 2)))

    return UNSPSC_Dict(UNSPSC_df)

