import pandas as pd
import glob

# Get the list of file paths
filepaths = glob.glob("Project 5- Excel to pdf invoice\\Invoice\\*.xlsx")

for filepath in filepaths:
    df=pd.read_excel(filepath,sheet_name='Sheet 1')
    print(df)