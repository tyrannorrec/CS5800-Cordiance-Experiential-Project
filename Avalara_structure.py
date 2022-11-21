import numpy as np
import pandas as pd
import os 
import re
import time

class ReadFile:

    # initialize a map to store the taxid and its corresponding valid key words
    def __init__(self):
        self.dict = {}
        self.manual_display()

    # interactive display interface
    def manual_display(self):

        print("What would you like to do? \n") 
        
        options = int(input("1. Peek a file. \n" +
                            "2. Read a file. \n" +
                            "3. Write map to file.\n" +
                            "4. Nothing, quit the program. \n:"))

        
        match options:
            case 1:
                print("Available file to read in: ")
                self.peek()
                self.manual_display()

            case 2:
                self.read()
                print(f"Total {len(self.dict)} entries")
                self.manual_display()

            case 3:
                self.write()
                self.manual_display()

            case 4:
                print("bye")
                return
                    
            case _:
                print("Invalid input, try again...")
                return

    # Peek the information of a valid data input file within the current working directory
    def peek(self):
        x = os.listdir('./')
        available_file_input = {}
        
        count = 1;
        for file in x:
            if file.endswith('.xlsx') and file[0].isalpha:
                available_file_input[count] = file
                count += 1

        # listing the available files to read        
        print("******************************************************************")
        for k,v in available_file_input.items():
            print(f"{k}: {v}")
        print("******************************************************************")

        # prompt user to choose file to read
        file_index = int(input("\nWhich file would you like to read?\n" +
                                   "Note: Only input the list number of file you want to read in.\n:"))  

        # file index must be valid
        try:

            xls = pd.ExcelFile(available_file_input[file_index])
            sheet_count = 1
            available_sheets = {}
            for sheet in xls.sheet_names:
                available_sheets[sheet_count] = sheet
                sheet_count += 1

            print(f"Available sheets in {available_file_input[file_index]} are \n{available_sheets}\n")
            
        except:
            print("Not a valid input, try agian....\n")
            time.sleep(0.5) # sleep for 1 second
            self.peek()

    # Read the input file and print the ds
    def read(self):
        df_ava = pd.read_excel('Avalara_goods_and_services.xlsx', 
                    'goods_and_services',
                    skiprows=1)

        build_map = Avalara_Listings(df_ava)

        self.dict = build_map.build()
        self.print()

    # Write to a csv file with all map information
    def write(self):
        print("Write successfully.\n")
    # print function to print the self.dict line by line
    def print(self):
        for k,v in self.dict.items():
            print(f"{k}: {v}")


# Init data structure, not fully implemented yet
class Avalara_Listings:

    def __init__(self, df):
        self.df = df
        self.map_ID_Keywords = {}
        # self.root_category = []

    def build(self):    
        
        # TODO:
        # currTopTaxCode, currSubTaxCode = "", ""

        # going through the avalara file line by line, pre-filter the keywords in description by length of 3
        # convert to case insensitive strings
        for i in self.df.index:
            tax_code_col = str(self.df['AvaTax System Tax Code'][i])
            
            if tax_code_col[-1] > '9' or tax_code_col[-1] < '0': # Skip invalid tax code
                continue
            tax_code_description = str(self.df['AvaTax System Tax Code Description'][i]).lower()

            word_list = []
            s = re.findall(r'\w+', tax_code_description) # regex expression to ignore any ascii values are not words
            for word in s:
                if len(word) > 3:
                    word_list.append(word)
                else:
                    continue
            
            self.map_ID_Keywords[tax_code_col] = word_list # add the valid listing to the map

            # if i > 5:
            #     return map_ID_Keywords
        return self.map_ID_Keywords

            # TODO: implement ds to store all information of each listing

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
         
# TODO: 
class top_category():


    def __init__(self):
        pass
# TODO:
class sub_category():

    def __init__(self):
        pass


def main():
    ReadFile()
    

if __name__ == "__main__":
    main()