import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

# Drop rows with missing values
df= df.dropna()

# Drop columns with missing values
df= df.dropna(axis=1)

#Enter a value
df["column_name"]= df["column_name"].fillna(0)

df.fillna(method="ffill") # Forward Fill
df.fillna(method='bfill') # Backward Fill

# Interpolation
df["column_name"] = df["column_name"].interpolate()

# Data Transformation
df = df.rename(columns = {"old_name":"new_name"})

df["column_name"] = df["column_name"].astype("float") # Change data type

df["column_name"]=pd.to_datetime(df["columnn_name"])

# Modify
df["column_name"]= df["existing_column"] * 2

# Concatenation of Datasets
combined = pd.concat([df1,df2],axis=0) # Combining along rows
combined = pd.conca([df1,df2],axis=0) # Combining along columns

# Merging the datasets
merged = pd.merge(df1,df2, on="common_column")
merged = pd.merge(df1,df2,how='left', one='common_column') # Left Join
merged = pd.merge(df1,df2, how='inner', on="common_column")

# Join dataframes
joined = df1.join(df2, how='inner')






