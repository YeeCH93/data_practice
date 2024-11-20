from matplotlib import pyplot as plt

# Data for the bar chart
past_years_averages = [82, 84, 83, 86, 74, 84, 90]
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006]
error = [1.5, 2.1, 1.2, 3.2, 2.3, 1.7, 2.4]

# Create a figure with specified width and height
plt.figure(figsize=(10, 8))

# Create a subplot and assign it to ax
ax = plt.subplot()

# Plot the bar chart with error bars
plt.bar(range(len(past_years_averages)), past_years_averages, color='#1f77b4', yerr=error, capsize=5)

# Set the axis limits
plt.axis([-0.5, 6.5, 70, 95])

# Set the x-axis ticks and labels
ax.set_xticks(range(len(years)))
ax.set_xticklabels(years)

# Add title and labels to the plot
plt.title("Final Exam Averages")
plt.xlabel("Year")
plt.ylabel("Test average")

# Save the figure to a file
#plt.savefig("bar_chart_with_error.png")

# Display the plot
plt.show()