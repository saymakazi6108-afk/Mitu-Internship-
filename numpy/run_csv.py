"""
steps for reading csv file 

1.create a folder 
2.In that folder create csv file and insert your data in it 
3.in the same folder create python file 
4.write actual code
5.in terminal you should in same directory where you have your all folders 
6.run file using command - python filename.py

"""

import pandas as pd

df = pd.read_csv("employee.csv")
print(df)

df.value_counts()
