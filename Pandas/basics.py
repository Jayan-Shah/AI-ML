import pandas as pd

s = pd.Series([10,20,30], index=["a","b","c"])
print(s)

data = {"Name": ["Alice","Bob"],"Age": [25,30]}
df = pd.DataFrame(data)
print(df)


# Loading Data from CSV,Excel and Other Sources

df = pd.read_csv("data.csv")
df = pd.read_excel("data.xlsx")

# Saving Data
df.to_csv("data.csv" , index=False) # Index = False is for prevent index to be printed
df.to_excel("data.xlsx", index = False)

#Viewing Data
print(df.head()) # head() - first 5 rows
print(df.tail(3)) # Last three rows
print(df.info()) # Summary of datasets
print(df.desceibe()) # Statistical Summary of datasets

print(df[["Name","Age"]]) # Selectng Multiple Columns
print(df[df["Age"]>25])

print(df.iloc[0]) # First row by position
print(df.iloc[:, 0]) # First column by position

print(df.loc[0]) # First row by index label
print(df.loc[:,"Name"]) #Selecting by name column




