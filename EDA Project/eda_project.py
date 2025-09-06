import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Titanic Dataset
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)

# Inspect Data
print(df.info()) # Shows age has some missing values
print(df.describe())

# Handle Missing Values
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"]= df["Embarked"].fillna(df["Embarked"].mode()[0])

# Remove duplicates
df = df.drop_duplicates()

# Filter data: Passemgers in first class
first_class = df[df["Pclass"]==1]
print("First Class Passengers: \n",first_class.head())

# Bar chart: Survival rate by class
survival_by_class = df.groupby("Pclass")["Survived"].mean()
survival_by_class.plot(kind='bar',color='skyblue')
plt.title("Survival Rate by class")
plt.ylabel("Survival Rate")
plt.show()

# Histogram of Age Distribution
sns.histplot(df["Age"],kde=True,bins=20,color='purple')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# Scatter plot: Age vs Fare
plt.scatter(df["Age"],df["Fare"],alpha=0.5,color='orange')
plt.title("Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()



