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



