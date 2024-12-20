from helper_functions import choose_statistic, population_distribution, sampling_distribution
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

# task 1: load in the spotify dataset
spotify_data = pd.read_csv('data/spotify_data.csv')

# task 2: preview the dataset
print(spotify_data.head())

# task 3: select the relevant column 
# (tempo = beats per minute (bpm) of each song
song_tempos = spotify_data.tempo

# Sampling Distribution Exploration
# task 5: plot the population distribution with the mean labeled
population_distribution(song_tempos)

# task 6: sampling distribution of the sample mean
sampling_distribution(song_tempos, 30, "Mean")
answer_sample_mean = """
The sample mean is an unbiased estimator since 147.36 is very close to the population mean of 147.47.
"""

# task 8: sampling distribution of the sample minimum
sampling_distribution(song_tempos, 30, "Minimum")
answer_sample_min = """
The sample minimum is a biased estimator because the mean of the sample minimums is consistently higher than the population minimum.
"""

# task 10: sampling distribution of the sample variance
sampling_distribution(song_tempos, 30, "Variance")
answer_sample_var = """
The mean of the sample variances is consistently slightly less than the population variance, meaning it is an unbiased estimator
Noted: np.var(x) to np.var(x, ddof=1) adjust for (n-1)
"""

# Calculating Probabilities
# task 13: calculate the population mean and standard deviation
population_mean = np.mean(song_tempos)
population_std = np.std(song_tempos)

# task 14: calculate the standard error
standard_error = population_std / (30 ** 0.5)

# task 15: calculate the probability of observing an average tempo of 140bpm or lower from a sample of 30 songs
print(stats.norm.cdf(140, population_mean, standard_error))

# task 16: calculate the probability of observing an average tempo of 150bpm or higher from a sample of 30 songs
print(1-stats.norm.cdf(150, population_mean, standard_error))
