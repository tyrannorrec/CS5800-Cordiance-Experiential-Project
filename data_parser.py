    import numpy as np
    import pandas as pd


    def avalara_parse():
        # read in file
        df_ava = pd.read_excel('Avalara_goods_and_services.xlsx', 
                        'goods_and_services',
                        header=1)
    
        # printing out column names                
        column_names = list(df_ava.columns.str.replace(' ', ''))
        # print(column_names)

        # set option to display all rows
        pd.set_option('display.max_rows', None)
        # print(df.to_string())

        # filtering the parent node (larger category type) ending by '0000'
        suffix = ['000000']
    

        filtered_col = df_ava[df_ava['AvaTax System Tax Code'].str.endswith(tuple(suffix), na=False)]
        print(filtered_col) 


    def UNSPSC_parse():
        df_UNSPSC = pd.read_excel('UNSPSC_English_excel.xlsx', 
                        'UNSPSC_English_excel',
                        skiprows=9)

        # printing out column names                
        # column_names = list(df_UNSPSC.columns.str.replace(' ', ''))
        # print(column_names)

        count = 0
        segment_title = []

        # Going through all segment title and add the distinct ones in to the segment_tile list
        for i in range(0, len(df_UNSPSC['Segment Title'])):
            str = df_UNSPSC['Segment Title'][i]
            if str not in segment_title:
                segment_title.append(str)
                count += 1
            else:
                continue
            
        # in case we want to resize the segment_title to represent in a matrix format
        # ending = 10 - count % 10
        # for i in range(0, ending):
        #     segment_title.append("null")

        # rows = 10
        # cols = int (len(segment_title) / 10)
        # org_segment_title = np.reshape(segment_title, (rows, cols))
        # print(org_segment_title)
        print(segment_title)
        print(f"The total number of distinct segment titles are: {count}")


    def main():
        # avalara_parse()
        UNSPSC_parse()


    if __name__ == "__main__":
        main()
