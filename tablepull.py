# tablepull.py
# Created by Andrew Lin
# Last edited: 7/6/2023
# 
# The tablepuller class uses pandas to extract tabular data from a provided
# html limk and writes them into an excel file. Each table will have a different
# sheet in the file. The tables are not named and are numbered in the order 
# they were found by the scraper
# 

import pandas as pd
import requests

class tablepuller:
    def __init__(self):
        pass

    # Name: pull
    # Input: a link to a webpage in str form
    # Output: writes all tabular data into an excel file titled "output.xlsx"
    # Purpose: scrapes an html page for tables and writes them into an excel file
    def pull(self, link):
        try:
            html = requests.get(link).content
            table_list = pd.read_html(html)
            index = 0
            with pd.ExcelWriter('output.xlsx') as writer:
                for table in table_list:
                    index += 1
                    table.to_excel(writer, sheet_name="sheet" + str(index))
        except:
            print("Error: No table data is present")