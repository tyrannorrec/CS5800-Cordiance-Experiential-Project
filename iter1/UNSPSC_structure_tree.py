import pandas as pd
import time

# ------------------------------------------------------------------------------------------------#

# Object represents tree structure holding all UNSPSC data.
# Hierarchy: UNSPSC_Tree -> UNSPSC_Segment -> UNSPSC_Family -> UNSPSC_Class -> UNSPSC_Commodity
# Attributes: df          -- Pandas data frame containing information read from excel file
#             childList   -- list of UNSPSC_Segment objects in tree
class UNSPSC_Tree:

    # Class initializer. Builds tree and prints time taken to build.
    def __init__(self, inDataFrame):

        self.df = inDataFrame
        self.childList = []

        print('>> Building UNSPSC tree...')
        start = time.time()
        self.build()
        print('>>>> Build complete. Process took %s seconds.\n' % (round((time.time() - start), 2)))

    # Parses data frame and builds tree. Called by initializer.
    def build(self):

        # Takes str param and returns list of words in str in lower caps.
        def getWordList(inStr):

            if isinstance(inStr, str) and len(inStr) > 0:
                return inStr.lower().split(' ')
            else:
                return []

        currSegmentID, currFamilyID, currClassID = 0, 0, 0
        currSegment, currFamily, currClass = None, None, None

        for i in self.df.index: # for every line in df

            if self.df['Segment'][i] != currSegmentID: # if new segment ID, create new segment
                currSegment = UNSPSC_Segment(self.df['Segment'][i], 
                getWordList(self.df['Segment Title'][i]), 
                getWordList(self.df['Segment Definition'][i]))
                self.childList.append(currSegment) # append to UNSPSC tree's segment list
                currSegmentID = self.df['Segment'][i] # update curr segment ID

            else: # if segment already exists

                if self.df['Family'][i] != currFamilyID: # if new family ID, create new family
                    currFamily = UNSPSC_Family(self.df['Family'][i], 
                    getWordList(self.df['Family Title'][i]), 
                    getWordList(self.df['Family Definition'][i]))
                    currSegment.childList.append(currFamily) # append to curr segment's family list
                    currFamilyID = self.df['Family'][i] # update curr family ID

                else: # if family already exists
                    
                    if self.df['Class'][i] != currClassID: # if new class ID, create new class
                        currClass = UNSPSC_Class(self.df['Class'][i],
                        getWordList(self.df['Class Title'][i]), 
                        getWordList(self.df['Class Definition'][i]))
                        currFamily.childList.append(currClass) # append to curr family's class list
                        currClassID = self.df['Class'][i] # update curr class ID

                    else: # if class already exists

                        currCommodity = UNSPSC_Commodity(self.df['Key'][i], self.df['Commodity'][i],
                        getWordList(self.df['Commodity Title'][i]), 
                        getWordList(self.df['Definition'][i]))
                        currClass.childList.append(currCommodity) # append to curr class's commodity list

    # Print function for testing.
    def printAll(self):

        for seg in self.segmentList:
            print(seg.id, ' ', seg.title, '')
            for fam in seg.familyList:
                print('\t', fam.id, ' ', fam.title)
                for cla in fam.classList:
                    print('\t\t', cla.id, '', cla.title)
                    for com in cla.commodityList:
                        print('\t\t\t', com.id, com.title)

# ------------------------------------------------------------------------------------------------#

# Object represents Segment in UNSPSC tree structure.
# Hierarchy: UNSPSC_Segment -> UNSPSC_Family -> UNSPSC_Class -> UNSPSC_Commodity
# Attributes: id          -- ID number of Segment (int)
#             title       -- list of words in name of Segment (list of str)
#             definition  -- list of words in description of Segment (list of str)
#             childList   -- list of UNSPSC_Segment objects in tree
class UNSPSC_Segment:

    def __init__(self, inID, inTitle, inDef):
        self.id = int(inID)
        self.title = inTitle
        self.definition = inDef
        self.childList = []

# ------------------------------------------------------------------------------------------------#

# Object represents Family in UNSPSC tree structure.
# Hierarchy: UNSPSC_Family -> UNSPSC_Class -> UNSPSC_Commodity
# Attributes: id          -- ID number of Family (int)
#             title       -- list of words in name of Family (list of str)
#             definition  -- list of words in description of Family (list of str)
#             childList   -- list of UNSPSC_Class objects in Segment
class UNSPSC_Family:

    def __init__(self, inID, inTitle, inDef):
        self.id = int(inID)
        self.title = inTitle
        self.definition = inDef
        self.childList = []

# ------------------------------------------------------------------------------------------------#

# Object represents Class in UNSPSC tree structure.
# Hierarchy: UNSPSC_Class -> UNSPSC_Commodity
# Attributes: id          -- ID number of Class (int)
#             title       -- list of words in name of Class (list of str)
#             definition  -- list of words in description of Class (list of str)
#             childList   -- list of UNSPSC_Commodity objects in Class
class UNSPSC_Class:

    def __init__(self, inID, inTitle, inDef):
        self.id = int(inID)
        self.title = inTitle
        self.definition = inDef
        self.childList = []

# ------------------------------------------------------------------------------------------------#

# Object represents Class in UNSPSC tree structure.
# Attributes: key         -- unique key of item (int)
#             id          -- ID number of Class (int)
#             title       -- list of words in name of Commodity (list of str)
#             definition  -- list of words in description of Commodity (list of str)
class UNSPSC_Commodity:

    def __init__(self, inKey, inID, inTitle, inDef):
        self.key = int(inKey)
        self.id = int(inID)
        self.title = inTitle
        self.definition = inDef

# ------------------------------------------------------------------------------------------------#

# Reads in UNSPSC excel file, converts to Pandas data frame, and returns a UNSPSC_Tree object.
def getTree():

    print('\n>> Converting UNSPSC file to data frame...')
    start = time.time()
    UNSPSC_df = pd.read_excel('../UNSPSC_English_excel.xlsx', 'UNSPSC_English_excel', skiprows=9)
    print('>>>> Conversion complete. Process took %s seconds.\n' % (round((time.time() - start), 2)))

    return UNSPSC_Tree(UNSPSC_df)

# ------------------------------------------------------------------------------------------------#

def main():
    UNSPSC_tree = getTree()

if __name__ == "__main__":
    main()
