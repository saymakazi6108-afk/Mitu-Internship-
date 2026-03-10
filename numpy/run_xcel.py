"""
steps for reading file 
1. create folder 
2. download pandas and openpyxl
3. create file for xcel data
4. create file for code 

"""
import pandas as pd

df = pd.read_excel("employees.xlsx")
print(df)
