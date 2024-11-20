from matplotlib import pyplot as plt
import numpy as np

# Data for the stacked bar chart
unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
As = [6, 3, 4, 3, 5]
Bs = [8, 12, 8, 9, 10]
Cs = [13, 12, 15, 13, 14]
Ds = [2, 3, 3, 2, 1]
Fs = [1, 0, 0, 3, 0]

# Create x-values for the bars
x = range(len(unit_topics))

# Calculate the starting heights for the Cs bars
c_bottom = np.add(As, Bs)

# Calculate the starting heights for the Ds bars
d_bottom = np.add(c_bottom, Cs)

# Calculate the starting heights for the Fs bars
f_bottom = np.add(d_bottom, Ds)

# Create a figure with specified width and height
plt.figure(figsize=(10, 8))

# Plot the As bars
plt.bar(x, As, label='As')

# Plot the Bs bars on top of the As bars
plt.bar(x, Bs, bottom=As, label='Bs')

# Plot the Cs bars on top of the As and Bs bars
plt.bar(x, Cs, bottom=c_bottom, label='Cs')

# Plot the Ds bars on top of the As, Bs, and Cs bars
plt.bar(x, Ds, bottom=d_bottom, label='Ds')

# Plot the Fs bars on top of the As, Bs, Cs, and Ds bars
plt.bar(x, Fs, bottom=f_bottom, label='Fs')

# Create a subplot and assign it to ax
ax = plt.subplot()

# Set the x-axis ticks and labels
ax.set_xticks(range(len(unit_topics)))
ax.set_xticklabels(unit_topics)

# Add title and labels to the plot
plt.title("Grade Distribution")
plt.xlabel("Unit")
plt.ylabel("Number of Students")

# Add a legend to identify each bar
plt.legend()

# Save the figure to a file
#plt.savefig("my_stacked_bar.png")

# Display the plot
plt.show()