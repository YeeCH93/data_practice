import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# load in the data
df = pd.read_csv("data/mushroom_data.csv")
print(df.head())

# list of all column headers
columns = df.columns.tolist()
for column in columns:
  #print(column)
  # Check if the column has only one unique value
  if df[column].nunique() <= 1:
    continue # skip this column
  
  # Check if the column has more than 50% missing values
  if df[column].isnull().mean() > 0.5:
    continue # skip

  # Check if the column has very low variability
  # If one value accounts for more than 95% of the data, it might not be informative
  if df[column].value_counts(normalize=True).max() > 0.95:
    continue # skip

  # Plot the countplot for the column if it passes all checks
  sns.countplot(df[column], order=df[column].value_counts().index)
  plt.xticks(rotation=30, fontsize=10)
  plt.xlabel(column, fontsize=12)
  plt.title(f"{column} Value Counts")
  #plt.show()
  plt.clf()









