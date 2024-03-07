import matplotlib.pyplot as plt
import numpy as np

# Generate random data for demonstration
np.random.seed(42)  # Set seed for reproducibility
categories = ['Category A', 'Category B', 'Category C', 'Category D']
data_values = np.random.randint(1, 100, size=len(categories))

# Bar chart
plt.figure(figsize=(8, 5))
plt.bar(categories, data_values, color='skyblue')
plt.title('Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()

# Pie chart
plt.figure(figsize=(8, 8))
plt.pie(data_values, labels=categories, autopct='%1.1f%%', startangle=90, colors=['lightcoral', 'lightgreen', 'lightblue', 'lightsalmon'])
plt.title('Pie Chart')
plt.show()

# Line graph
time_points = np.arange(1, len(categories) + 1)
plt.figure(figsize=(8, 5))
plt.plot(time_points, data_values, marker='o', linestyle='-', color='orange')
plt.title('Line Graph')
plt.xlabel('Time Points')
plt.ylabel('Values')
plt.show()
