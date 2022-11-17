import numpy as np
import pandas as pd


# not implemented yet
def parse():
    return 


def main():
    # read in file
    df = pd.read_excel('Avalara_goods_and_services.xlsx', 
                    'goods_and_services',
                    header=1)

    # printing out column names                
    column_names = list(df.columns.str.replace(' ', ''))
    # print(column_names)

    # filtering the parent node (larger category type) ending by '0000'
    suffix = ['0000']
   
    
    filtered_col = df[df['AvaTax System Tax Code'].str.endswith(tuple(suffix), na=False)]
    print(filtered_col)


if __name__ == "__main__":
    main()
