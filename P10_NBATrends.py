import numpy as np
import pandas as pd
from scipy.stats import pearsonr, chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns

np.set_printoptions(suppress=True, precision = 2)

nba = pd.read_csv('data/nba_games.csv')

# Subset Data to 2010 Season, 2014 Season
nba_2010 = nba[nba.year_id == 2010]
nba_2014 = nba[nba.year_id == 2014]

#print(nba_2010.head())
#print(nba_2014.head())

# Analyzing relationships between Quant (pts) and Categorical (fran_id)

# 1.Knicks and Nets points per game (year 2010)
knicks_pts_10 = nba_2010.pts[nba_2010["fran_id"] == "Knicks"]
#print(knicks_pts_10.head())

nets_pts_10 = nba_2010.pts[nba_2010["fran_id"] == "Nets"]
#print(nets_pts_10.head())

# 2.Calculate the difference between the two teams’ average points scored
diff_means_2010 = knicks_pts_10.mean() - nets_pts_10.mean()
print(f"On average, the Knicks scored about {diff_means_2010:.2f} more points per game than the Nets in 2010")

# 3.Overlapping histograms
## Knicks’ distribution seems to be shifted to the right
plt.hist(knicks_pts_10, alpha=0.8, normed=True, label='knicks')
plt.hist(nets_pts_10, alpha=0.8, normed=True, label='nets')
plt.legend()
plt.title("2010 Season")
plt.show()

# 4.Compare the 2010 games to 2014
## Knicks and Nets points per game (year 2014)
knicks_pts_14 = nba_2014.pts[nba_2014["fran_id"] == "Knicks"]
nets_pts_14 = nba_2014.pts[nba_2014["fran_id"] == "Nets"]

## mean difference
diff_means_2014 = knicks_pts_14.mean() - nets_pts_14.mean()
print(f"On average, the Knicks scored about {diff_means_2014:.2f} more points per game than the Nets in 2014")

## Overlapping histograms
plt.clf() # clear previous plot
plt.hist(knicks_pts_14, alpha=0.8, normed=True, label='knicks')
plt.hist(nets_pts_14, alpha=0.8, normed=True, label='nets')
plt.legend()
plt.title("2014 Season")
plt.show()

# summarize
print(f"In 2014, the Knicks and Nets had a mean score difference of {diff_means_2014:.2f} points, indicating similar performance. The overlapping histograms confirm this similarity.")

# 5.side-by-side boxplot with points scored for team in 2010
plt.clf()
sns.boxplot(data = nba_2010, x='fran_id', y='pts')
plt.show()

print("The boxplot shows the Knicks have a higher median points scored than the Nets, indicating a significant difference. There is also some difference between the Knicks and Celtics. However, the Thunder and Spurs have similar medians to the Knicks. This suggests fran_id and pts are associated, with some teams scoring differently on average.")

print("---------------------------------------")

# Analyzing relationships between Categorical variables (game_result and game_location)

# 6.Calculate a table of frequencies that shows the counts of game_result and game_location for year 2010
location_result_freq_10 = pd.crosstab(nba_2010.game_result, nba_2010.game_location)

print("Table of Frequencies")
print(location_result_freq_10)
print("Interpret the result")
print("Home Games (H): Teams won 120 games and lost 105 games.")
print("Away Games (A): Teams won 92 games and lost 133 games.")
print("Teams tend to win more games at home compared to away")

# 7.Convert this table of frequencies to a table of proportions
location_result_proportions_10 = (location_result_freq_10 / len(nba_2010)).round(2)
print("Table of Proportions")
print(location_result_proportions_10)

# 8.Expectation contingency table (if there were no association) and Chi-Square statistic
chi2, pval, dof, expected = chi2_contingency(location_result_freq_10)

expected_df = pd.DataFrame(expected, index=['L', 'W'], columns=['A', 'H'])

print("Table of Frequencies (Actual)")
print(location_result_freq_10)
print("Table of Frequencies (Expectation")
print(expected_df)
print(f"Chi-Square statistic: {chi2}")

print("Actual Home-Win is 120 higher than the Expected Home-Win value 106.")
print(f"The Chi-Square value of {chi2:.2f} suggests there is some association between game location and game result")

print("---------------------------------------")

# Analyzing Relationships Between Quantitative Variables (forecast and point_diff)

# 9. Covariance btw forecast and point_diff
point_diff_forecast_cov_10 = np.cov(nba_2010.forecast, nba_2010.point_diff)
print("Covariance Matrix: forecast vs. point_diff")
print(point_diff_forecast_cov_10)
print("Covariance: 1.37")

# 10.The strength of the correlation btw forecast and point_diff
point_diff_forecast_corr_10, p = pearsonr(nba_2010.forecast, nba_2010.point_diff)
print(f"The correlation: {point_diff_forecast_corr_10:.2f} (moderate positive relationship)")

# 11.Scatter plot of forecast (x-axis) and point_diff (y-axis)
plt.clf()
plt.scatter('forecast', 'point_diff', data=nba_2010)
plt.xlabel('Forecasted Win Prob.')
plt.ylabel('Point Differential')
plt.text(0.7, -30, f'Correlation: {point_diff_forecast_corr_10:.2f}', fontsize=12, color='red')
plt.show()

