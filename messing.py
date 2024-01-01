import matplotlib.pyplot as plt
import numpy as np
import pandas as pd




# Load the CSV file into a DataFrame
data = pd.read_csv('penguins.csv')

# Extract values from the 'bill_length_mm' column
bill_length_values = data['bill_length_mm']

np.unique(bill_length_values)

# Display the extracted values
#print(np.unique(bill_length_values))

#we extracted the unique values but it didn't help, all values were different, we decided to print all values and add them into a histogram



# Load the CSV file into a DataFrame
data = pd.read_csv('penguins.csv')

# Extract values from the 'bill_length_mm' column
bill_length_values = data['bill_length_mm']

# Sort the 'bill_length_mm' values
sorted_bill_lengths = bill_length_values.sort_values()

# Create an array of indices for the x-axis
x_indices = range(len(sorted_bill_lengths))

# Plot the sorted 'bill_length_mm' values in a bar plot
plt.bar(x_indices, sorted_bill_lengths)

plt.title('Sorted Bill Lengths')
plt.xlabel('Index')
plt.ylabel('Bill Length (mm)')

plt.show()



import seaborn as sns

penguins = sns.load_dataset("penguins")

species_counts = penguins['species'].value_counts().reset_index()
species_counts.columns = ['species', 'count']


# Create a violin plot for the 'species' variable
sns.catplot(data=species_counts, x='species', y='count', kind="bar")






import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

datafile = pd.read_csv('documentation/iris_data.csv')
datafile.columns = ['sepal length', 'sepal width', 'petal length', 'petal width', 'flower class']

# Group data by flower class and compute min and max values for petal length
datatable = datafile.groupby('flower class')['petal length'].agg(['min', 'max'])

# Create subplots with 1 row and 1 column
fig, ax = plt.subplots(1,1)
#Scatter plot the min and max values for each flower class
ax.scatter(datatable.index, datatable['min'], color='blue')
ax.scatter(datatable.index, datatable['max'], color='yellow')
ax.set_xlabel('Flower Class max/min')
ax.set_ylabel('Petal Length')
plt.suptitle('Petal Length',weight='bold')


datatable = datafile.groupby('flower class')['sepal length'].agg(['min', 'max'])
fig, ax = plt.subplots(1,1)
ax.scatter(datatable.index, datatable['min'], color='blue')
ax.scatter(datatable.index, datatable['max'], color='yellow')
ax.set_xlabel('Flower Class')
ax.set_ylabel('sepal length')
plt.suptitle('Sepal Length',weight='bold')


datatable = datafile.groupby('flower class')['sepal width'].agg(['min', 'max'])
fig, ax = plt.subplots(1,1)
ax.scatter(datatable.index, datatable['min'], color='blue')
ax.scatter(datatable.index, datatable['max'], color='yellow')
ax.set_xlabel('Flower Class')
ax.set_ylabel('sepal width')
plt.suptitle('Sepal Width',weight='bold')


datatable = datafile.groupby('flower class')['petal width'].agg(['min', 'max'])
fig, ax = plt.subplots(1,1)
ax.scatter(datatable.index, datatable['min'], color='blue')
ax.scatter(datatable.index, datatable['max'], color='yellow')
ax.set_xlabel('Flower Class')
ax.set_ylabel('petal width')
plt.suptitle('Petal Width',weight='bold')
plt.show()
plt.savefig('scatterplot.png')