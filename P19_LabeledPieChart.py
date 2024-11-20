from matplotlib import pyplot as plt

# Data for the pie chart
unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
num_hardest_reported = [1, 3, 10, 15, 1]

# Create a figure with specified size
plt.figure(figsize=(10, 8))

# Plot the pie chart with labels and percentage
plt.pie(num_hardest_reported, labels=unit_topics, autopct="%d%%")

# Set the axes to be equal for a perfect circle
plt.axis('equal')

# Add a title to the pie chart
plt.title("Hardest Topics")

# Save the pie chart to a file
#plt.savefig("my_pie_chart.png")

# Display the pie chart
plt.show()