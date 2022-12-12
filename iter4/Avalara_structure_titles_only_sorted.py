import pandas as pd
import re
import time

class Ava_Dict:

    # Initializes a dictionary where key = tax ID and value = list of key words
    def __init__(self):
        self.data = {}
        self.results = None
        self.read()

    # Reads Avalara data frame into self.dict
    def read(self):

        start = time.time()
        print('>> Building Avalara dictionary...')
        df_ava = pd.read_excel('Avalara_goods_and_services.xlsx', 
                    'goods_and_services',
                    skiprows=1)

        builder = Avalara_Dict_Builder(df_ava)
        self.data = builder.build()
        #self.results = builder.results

        #self.print()
        print('>>>> Build complete. Process took %s seconds.\n' % (round((time.time() - start), 2)))
    
    # Prints self.dict contents
    def print(self):
        for k,v in self.data.items():
            print(f"{k}: {v}")


# Utility class to build dictionary of Avalara items
class Avalara_Dict_Builder:

    def __init__(self, df):
        self.df = df
        self.map_ID_Keywords = {}
        #self.results = None

    def build(self):    

        # Declare pandas data frame to store results
        #self.results = pd.DataFrame(columns = ['Ava Tax Code', 'Ava Description', 'Commodity ID'])
        #self.results.set_index(['Ava Tax Code'], inplace = True)

        # Going through the avalara file line by line, pre-filter the keywords in description by length of 3
        # convert to case insensitive strings
        for i in self.df.index:

            if i > 10:
                break

            tax_code_col = str(self.df['AvaTax System Tax Code'][i])
            
            if tax_code_col[-1] > '9' or tax_code_col[-1] < '0': # Skip invalid tax code
                continue

            tax_code_description = str(self.df['AvaTax System Tax Code Description'][i]).lower()

            curr_tax_list = []

            s = re.findall(r'\w+', tax_code_description) # regex expression to ignore any ascii values are not words
            for word in s:
                if len(word) > 3:
                    curr_tax_list.append(word)
                else:
                    continue
            curr_tax_list = [*set(curr_tax_list)]
            curr_tax_list.sort()
            
            self.map_ID_Keywords[tax_code_col] = curr_tax_list # add the valid listing to the map
            #newFrame = pd.DataFrame(columns = {'Ava Tax Code': tax_code_col, 'Ava Description': tax_code_description})
            #newFrame.set_index('Ava Tax Code', inplace = True)
            #self.results = pd.concat([self.results, newFrame])
            #self.results.loc[len(self.results.index)] = [tax_code_col, tax_code_description, float('Nan')]

        return self.map_ID_Keywords
