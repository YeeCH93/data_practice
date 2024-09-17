# Load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import data
students = pd.read_csv('data/students.csv')

# Print first few rows of data
#print(students.head())

# Print summary statistics for all columns
#print(students.describe(include='all'))

# Summarize a typical student grade
## absences column with the same method

# Calculate mean
math_g_mean = students['math_grade'].mean()
print(f"Average math grade: {math_g_mean:.2f}")

# Calculate median
math_g_median = students['math_grade'].median()
print(f"Median math grade: {math_g_median}")

# Calculate mode
math_g_mode = students['math_grade'].mode()[0]
print(f"Mode math grade: {math_g_mode}")

print(f"The different between mean and mode: {math_g_mean - math_g_mode:.1f}")
print(f"The different between median and mode: {math_g_median - math_g_mode}")

# Summarize the spread of student grades

# Calculate range
math_g_range = students['math_grade'].max() - students['math_grade'].min()
print(f"Range math grade: {math_g_range}")

# Calculate standard deviation
math_g_sd = students['math_grade'].std()
print(f"Standard Deviation math grade: {math_g_sd:.2f}")
print(f"Standard deviation: {math_g_sd:.2f}, mean: {math_g_mean:.2f}. About two-thirds of students score between {math_g_mean - math_g_sd:.2f} and {math_g_mean + math_g_sd:.2f}.")

# Calculate MAD
math_g_mad = students['math_grade'].mad()
print(f"Mean Absolute Deviation math grade: {math_g_mad:.2f}")

# Visualize the distribution of student grades

# Create a histogram of math grades
sns.histplot(x='math_grade', data=students)
plt.show()
plt.clf()

# Create a box plot of math grades
sns.boxplot(x='math_grade', data=students)
plt.show()
plt.clf()

# Summarize mother's jobs
## address and Fjob column with the same method

# Calculate number of students with mothers in each job category
mothers_job_counts = students['Mjob'].value_counts()
print(mothers_job_counts)

# Calculate proportion of students with mothers in each job category
mothers_job_proportions = students['Mjob'].value_counts(normalize = True).round(2)
print(mothers_job_proportions)

# Visualize the distribution of mothers' jobs

# Create bar chart of Mjob
sorted_order = students['Mjob'].value_counts().index
sns.countplot(x='Mjob', data=students, order=sorted_order)
plt.show()
plt.clf()

# Create pie chart of Mjob
students.Mjob.value_counts().plot.pie()
plt.show()

