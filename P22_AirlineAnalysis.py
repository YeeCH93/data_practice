import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels
import matplotlib.pyplot as plt
import math


## Read in Data
flight = pd.read_csv("data/flight.csv")
print(flight.head())

# Univariate Analysis

## Task 1
# Create a boxplot for coach prices
sns.boxplot(y='coach_price', data=flight)
plt.title('Coach Ticket Price')
#plt.show()
plt.clf()

# Calculate mean and median 
coach_price_mean = flight['coach_price'].mean()
coach_price_median = flight['coach_price'].median()
# Print the statement
statement = f"The mean coach price is ${coach_price_mean:.2f} and the median coach price is ${coach_price_median:.2f}."
print(statement)


## Task 2
# Filter the data for 8-hour flights
eight_hour_flights = flight[flight['hours'] == 8]
# Create a boxplot for coach prices of 8-hour flights
sns.boxplot(y='coach_price', data=eight_hour_flights)
plt.title('Coach Ticket Prices for 8-Hour Flights')
#plt.show()
plt.clf()

# Calculate mean and median for 8-hour flights
mean_8hr = eight_hour_flights['coach_price'].mean()
median_8hr = eight_hour_flights['coach_price'].median()

# Print the statement
statement_8hr = f"The mean coach price for 8-hour flights is ${mean_8hr:.2f} and the median is ${median_8hr:.2f}."
print(statement_8hr)

## Task 3
# Subset the data to exclude extreme outliers
reasonable_delays = flight[flight['delay'] <= 60]
# Create a histogram for delay times
sns.histplot(reasonable_delays['delay'], bins=30)
plt.xlabel('Delay (minutes)')
plt.title('Distribution of Flight Delays')
#plt.show()
plt.clf()

# Bivariate Analysis

## Task 4
# Take a random sample of the data
sampled_flight = flight.sample(frac=0.1, random_state=1)
# Create a scatterplot with a LOWESS smoother using the sample data
sns.lmplot(x='coach_price', y='firstclass_price', data=sampled_flight, line_kws={'color': 'black'}, lowess=True, scatter_kws={'alpha': 0.5})
plt.title('Relationship Between Coach and First-Class Prices')
#plt.show()
plt.clf()

## Task 5
# Histogram for inflight meal
sns.histplot(data=flight, x='coach_price', hue='inflight_meal', bins=30, kde=True)
plt.title('Coach Price Distribution by Inflight Meal')
plt.xlabel('Coach Price')
#plt.show()
plt.clf()

# Histogram for inflight entertainment
sns.histplot(data=flight, x='coach_price', hue='inflight_entertainment', bins=30, kde=True)
plt.title('Coach Price Distribution by Inflight Entertainment')
plt.xlabel('Coach Price')
#plt.show()
plt.clf()

# Histogram for inflight WiFi
sns.histplot(data=flight, x='coach_price', hue='inflight_wifi', bins=30, kde=True)
plt.title('Coach Price Distribution by Inflight WiFi')
plt.xlabel('Coach Price')
#plt.show()
plt.clf()

## Task 6
# Create a scatterplot for hours vs. passengers using the sampled data with jitter
sns.lmplot(x='hours', y='passengers', data=sampled_flight, x_jitter=0.25, scatter_kws={"s": 5, "alpha": 0.2}, fit_reg=False)
plt.title('Number of Passengers vs. Flight Length')
plt.xlabel('Flight Length (hours)')
plt.ylabel('Number of Passengers')
#plt.show()
plt.clf()

# Multivariate Analysis

## Task 7
# Create a scatterplot for coach and first-class prices with hue for weekend
sns.lmplot(x='coach_price', y='firstclass_price', data=sampled_flight, hue='weekend', line_kws={'color': 'black'}, lowess=True, scatter_kws={'alpha': 0.5})
plt.title('Coach vs. First-Class Prices: Weekend vs. Weekday')
plt.xlabel('Coach Price')
plt.ylabel('First-Class Price')
#plt.show()
plt.clf()

## Task 8
# Define the order of the days
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# Create a boxplot for coach prices by day of the week with hue for redeye
sns.boxplot(x='day_of_week', y='coach_price', hue='redeye', data=flight, order=day_order)
plt.title('Coach Prices by Day of the Week: Redeye vs. Non-Redeye')
plt.xlabel('Day of the Week')
plt.ylabel('Coach Price')
plt.xticks(rotation=45)
#plt.show()
plt.clf()
