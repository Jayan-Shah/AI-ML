import pandas as pd

data = {
    "Class":["A","B","B","C","C","A"],
    "Score":[85,90,98,72,95,80],
    "Age": [15,16,15,17,16,18]
}

df = pd.DataFrame(data)
print("Original Dataset\n", df)

grouped = df.groupby("Class").mean()
print(grouped)
# O/P:
# Class   Score   Age          
# A       82.5  16.5
# B       94.0  15.5
# C       83.5  16.5


stats = df.groupby("Class").agg(
    {"Score":["mean","max","min"], "Age":["mean","max","min"]}
)
print("Stats are \n",stats)

