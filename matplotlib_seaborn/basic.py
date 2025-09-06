import matplotlib.pyplot as plt




# Basic Plot
x = [1,2,3,5]
y= [10,20,25,40]
plt.plot(x,y)
plt.show()

# Line Plot
plt.plot([1,2,3], [10,20,30], label = "Trend")
plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()

# Bar Chart
categories = ["A","B","C"]
values = [10,15,7]
plt.bar(categories,values,color="blue")
plt.title("Bar Chart")
plt.show()


# Histogram
data = [1,2,3,2,3,3,4,4,5]
plt.hist(data,bins = 9,color = "red", edgecolor = "orange")
plt.title("Histogram")
plt.show()

# Scatter Plot
x = [1,2,3,44,5]
y= [10,12,25,30,45]
plt.scatter(x,y,color = "purple")
plt.title("Scatter Plot")
plt.legend(["Dataset-1"])
plt.show()

# More design
plt.plot([1,2,3], [10,20,30], label = "Trend",color="orange",linestyle="--",marker="x")
plt.show()


