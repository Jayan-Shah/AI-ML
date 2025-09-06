import pandas as pd

# Group column
grouped = df.groupby("column_name")

for name,group in grouped:
    print(name)
    print(group)


grouped.mean()
grouped.sum()
# Using groupby with aggregation function
df.groupby("category_columm")["numerc_column"].mean()
df.groupby("category_column").agg({"numeric_column":["mean","max","min"]})

# Using pivot_table
pivot = df.pivot_table(
    values = "numeric_column",
    index = " category_column",
    aggfunc = "mean"
)

# Using range_func

def range_func(x):
    return x.max() - x.min()

df.groupby("category_column")["numeric_column"].agg(range_func)

# Calculating Summary for Grouped Data
df.groupby("category_columm")["numerc_column"].mean()
df.groupby("category_columm")["numerc_column"].max()
df.groupby("category_columm")["numerc_column"].min()

