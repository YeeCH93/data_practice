# import libraries
import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp
from scipy.stats import binom_test

# load data
heart = pd.read_csv('data/heart_disease.csv')
yes_hd = heart[heart.heart_disease == 'presence']
no_hd = heart[heart.heart_disease == 'absence']

# Cholesterol Analysis
print("----- Cholesterol Analysis -----")
# Test1: Analysis of Cholesterol Levels in Patients with Heart Disease
chol_hd_y = yes_hd.chol
chol_hd_y_mean = np.mean(chol_hd_y)
print(f"- The mean cholesterol level: {chol_hd_y_mean}")

## hypothesis test
t_stat, p_value = ttest_1samp(chol_hd_y, 240)
one_sided_p_value = p_value / 2
print(f"- The one-sided p-value is {one_sided_p_value:.4f}. Since it is less than 0.05, we reject the null hypothesis and conclude that heart disease patients have an average cholesterol level significantly greater than 240 mg/dl.")

print("------------------------------")

# Test2: Analysis of Cholesterol Levels in Patients without Heart Disease
chol_hd_n = no_hd.chol
chol_hd_n_mean = np.mean(chol_hd_n)
print(f"- The mean cholesterol level: {chol_hd_n_mean}")

## hypothesis test
t_stat, p_value = ttest_1samp(chol_hd_n, 240)
one_sided_p_value = p_value / 2
print(f"- The one-sided p-value is {one_sided_p_value:.4f}. Since it is greater than 0.05, we cannot reject the null hypothesis, and we do not have enough evidence to conclude that patients without heart disease have an average cholesterol level significantly greater than 240 mg/dl.")

# Fasting Blood Sugar Analysis
print("----- Fasting Blood Sugar Analysis -----")
# calculate number of patients total
num_patients = len(heart)
print(f"- The total number of patients in the dataset is {num_patients}.")

# calculate number of patients with fbs>120
num_highfbs_patients = np.sum(heart.fbs == 1)
print(f"- The number of patients with fasting blood sugar greater than 120 mg/dl is {num_highfbs_patients}.")

# calculate 8% of sample size
expected_diabetes_patients = num_patients * 0.08
print(f"- Based on the sample size, approximately {expected_diabetes_patients:.0f} patients are expected to have diabetes, which is different from the observed number with fasting blood sugar > 120 mg/dl ({num_highfbs_patients}).")

# run binomial test
pval = binom_test(num_highfbs_patients, num_patients, 0.08, alternative='greater')
print(f"- The p-value from the binomial test is {pval:.6f}. Since it is less than 0.05, we reject the null hypothesis and conclude that the sample likely comes from a population where more than 8% of people have fasting blood sugar > 120 mg/dl.")

print("----- END -----")

