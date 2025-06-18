import pandas as pd

df = pd.read_excel('./challenge.xlsx', sheet_name="Sheet1")

my_nome = df["First Name"]
my_sobrenome = df["Last Name "]

print(my_sobrenome)

