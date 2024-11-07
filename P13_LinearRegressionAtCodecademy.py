# Load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# Read in the data
codecademy = pd.read_csv('data/codecademy.csv')

# Print the first five rows
print(codecademy.head(5))

# Model the relationship between quiz score and number of completed content items

# Create a scatter plot of score vs completed
plt.scatter(codecademy.completed, codecademy.score)

# Show then clear plot
plt.show()
plt.clf()

# Fit a linear regression to predict score based on prior lessons completed
model = sm.OLS.from_formula('score ~ completed', data = codecademy)
results = model.fit()
print(results.params)

# Intercept interpretation:
print(f"A learner who has previously completed 0 content items is expected to earn a quiz score of {results.params[0]:.1f} points.")

# Slope interpretation:
print(f"Students who have completed one additional prior content item are expected to score {results.params[1]:.1f} points higher on the quiz.")

# Plot the scatter plot with the line on top
plt.scatter(codecademy.completed, codecademy.score)
plt.plot(codecademy.completed, results.predict(codecademy))

# Show then clear plot
plt.show()
plt.clf()

# Predict score for learner who has completed 20 prior lessons
newdata = {'completed':[20]}
predicted_score = results.predict(newdata)
print(f"Predicted score for a learner who has completed 20 content items: {predicted_score[0]:.1f}")

# Calculate fitted values
fitted_values = results.predict(codecademy)

# Calculate residuals
residuals = codecademy.score - fitted_values

# Check normality assumption
plt.hist(residuals)

# Show then clear the plot
plt.show()
plt.clf()

# Check homoscedasticity assumption
plt.scatter(fitted_values, residuals)

# Show then clear the plot
plt.show()
plt.clf()

# Do learners who take lesson A or B perform better on the quiz?

# Create a boxplot of score vs lesson
sns.boxplot(x='lesson', y='score', data=codecademy)

# Show then clear plot
plt.show()
plt.clf()

# Fit a linear regression to predict score based on which lesson they took
model = sm.OLS.from_formula('score ~ lesson', data=codecademy)
results = model.fit()
print(results.params)

# Calculate and print the group means and mean difference (for comparison)
print(codecademy.groupby('lesson').mean().score)

# Use `sns.lmplot()` to plot `score` vs. `completed` colored by `lesson`
sns.lmplot(x='completed', y='score', hue='lesson', data=codecademy)
plt.show()
plt.clf()