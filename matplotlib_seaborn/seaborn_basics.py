import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# basic plot
data = np.random.rand(5,5)
sns.heatmap(data,annot=True,cmap = "coolwarm")
plt.title("Heatmap")
plt.show()

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
del df['species']
correlation_matrix =df.corr()

sns.heatmap(correlation_matrix,annot=True,cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# pairplot of df
sns.pairplot(df)
plt.show()
