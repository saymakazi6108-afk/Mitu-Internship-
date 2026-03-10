"""
steps for reading json file 
1.create a folder , in which create json file 
2.in json file write data 
3.fetch in python file using read_json() 

"""
import pandas as pd

df = pd.read_json("employees.json")
print(df)
