# Dataset:-  https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv

import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

print("\nFirst 5 rows\n", df.head())
print("\nLast 3 rows\n", df.tail(3))
print("\nInformation\n", df.info())
print("\nDescription\n", df.describe())

selected_columns = df[["species","sepal_length"]]
print("\nSelected Columns are:\n", selected_columns)

filtered_rows = df[(df["sepal_length"]>5.0) & (df["species"]=='setosa')]
print("\nFiltered Rows\n",filtered_rows)


