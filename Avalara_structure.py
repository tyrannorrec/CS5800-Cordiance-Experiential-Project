import numpy as np
import pandas as pd
import os 
import re

class ReadFile:

    # user manual
    def __init__(self):
        self.dict = {}
        print("What would you like to do? \n") 
        
        options = int(input("1. Peek a file. \n" +
                            "2. Read a file. \n" +
                            "3. Nothing, quit the program. \n:"))

        
        match options:
            case 1:
                print("Available file to read in: ")
                self.peek()

            case 2:
                self.read()
                print(f"Total {len(self.dict)} entries")

            case 3:
                print("bye")
                return
                    
            case _:
                print("Invalid input, try again...")
                return
    
    # Peek the information of a valid data input file
    def peek(self):
        # take a peek of the file
        x = os.listdir('./')
        available_file_input = {}
        
        count = 1;
        for file in x:
            if (file).endswith('.xlsx'):
                available_file_input[count] = file
                count += 1

        print(available_file_input)
        
        file_index = int(input("\nWhich file would you like to read?\n" +
                                   "Note: Only input the list number of file you want to read in.\n:"))  

        try:
            xls = pd.ExcelFile(available_file_input[file_index])
        
        except:
            print("Try agian....")

        sheet_count = 1
        available_sheets = {}
        for sheet in xls.sheet_names:
            available_sheets[sheet_count] = sheet
            sheet_count += 1

        print(f"Available sheets in {available_file_input[file_index]} are \n{available_sheets}")
    # Read the input file and print the ds
    def read(self):
        df_ava = pd.read_excel('Avalara_goods_and_services.xlsx', 
                    'goods_and_services',
                    skiprows=1)

        build_map = Avalara_Listings(df_ava)

        self.dict = build_map.build()

        self.print()
        
    def print(self):
        for k,v in self.dict.items():
            print(f"{k}: {v}")


#creating data structure
class Avalara_Listings:

    def __init__(self, df):
        self.df = df
        self.root_category = []

    def build(self):    
        map_ID_Keywords = {}
        
        currTopTaxCode, currSubTaxCode = "", ""

        for i in self.df.index:
            tax_code_col = str(self.df['AvaTax System Tax Code'][i])
            if not tax_code_col[-1].isdigit:
                continue
            tax_code_description = str(self.df['AvaTax System Tax Code Description'][i]).lower()

            word_list = []
            s = re.findall(r'\w+', tax_code_description)
            for word in s:
                if len(word) > 3:
                    word_list.append(word)
                else:
                    continue
            
            map_ID_Keywords[tax_code_col] = word_list

            if i > 10:
                return map_ID_Keywords
        return map_ID_Keywords

            # if tax_code_col[0].isalpha() and tax_code_col[1:].isdigit():
            #     if tax_code_col != currTopTaxCode:
                    
        

            # if tax_code_col[0].isalpha() and tax_code_col[2:].isdigit():
            #     if i < 10:
            #         print(tax_code_col)
            # if tax_code_col.isalpha:

            # filtering the parent node (larger category type) ending by '000000'
            # if tax_code_col.endswith(tuple(suffix)):
                # ls.append(tax_code_col)
        
        # print(len(ls))
         

class top_category():

    def __init__(self):
        pass

class sub_category():

    def __init__(self):
        pass


def main():
    ReadFile()
    

if __name__ == "__main__":
    main()