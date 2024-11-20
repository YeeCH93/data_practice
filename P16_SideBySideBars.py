from matplotlib import pyplot as plt

# Data for the bar chart
unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
middle_school_a = [80, 85, 84, 83, 86]
middle_school_b = [73, 78, 77, 82, 86]

# Function to create x-values for the bars
def create_x(t, w, n, d):
    return [t*x + w*n for x in range(d)]

# Create x-values for Middle School A and B
t = 2  # Total number of data sets
w = 0.8  # Width of each bar
n = 1  # Position of the first data set
d = 5  # Number of topics
school_a_x = create_x(t, w, n, d)

n = 2  # Position of the second data set
school_b_x = create_x(t, w, n, d)

# Calculate middle x-values for x-ticks
middle_x = [(a + b) / 2.0 for a, b in zip(school_a_x, school_b_x)]

# Create a figure with specified width and height
plt.figure(figsize=(10, 8))

# Create a subplot and assign it to ax
ax = plt.subplot()

# Plot the bars for Middle School A and B with labels for the legend
plt.bar(school_a_x, middle_school_a, color='blue', label='Middle School A')
plt.bar(school_b_x, middle_school_b, color='orange', label='Middle School B')

# Set the x-axis ticks and labels
ax.set_xticks(middle_x)
ax.set_xticklabels(unit_topics)

# Add title and labels to the plot
plt.title("Test Averages on Different Units")
plt.xlabel("Unit")
plt.ylabel("Test Average")

# Create the legend
plt.legend()

# Save the figure to a file
# plt.savefig("side_by_side.png")

# Display the plot
plt.show()