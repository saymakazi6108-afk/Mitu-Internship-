import pandas as pd

data = {
    "id": [1, 2, 3, 4],
    "name": ["Ayaan", "Sara", "Zara", "Ali"],
    "department": ["IT", "HR", "IT", "Finance"],
    "salary": [50000, 60000, 55000, 65000]
}

df = pd.DataFrame(data)
df.to_excel("employees.xlsx", index=False)

print("Excel file created successfully")


df = pd.read_excel("employees.xlsx")
print(df)