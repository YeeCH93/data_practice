# Import pandas with alias
import pandas as pd

# Read in the census dataframe
census = pd.read_csv('data/census_data.csv', index_col=0)

# Inspect DataFrame
#print(census.head(5))

# Check data types
# print(census.dtypes)

# Inspect birth_year column
# print(census['birth_year'].unique())
## birth_year column contain 'missing' value

# Replace 'missing' value with 1967
census['birth_year']  = census['birth_year'].replace(['missing'], 1967)
# print(census['birth_year'].unique())

# change birth_year data type to int
census['birth_year'] = census['birth_year'].astype(int)
#print(census.dtypes)

# Find average birth_year
avg_birth_year = census['birth_year'].mean()
print(f"The average birth year is: {avg_birth_year:.0f}")

# Change higher_tax data type to Categorical
# print(census['higher_tax'].unique())
census['higher_tax'] = pd.Categorical(census['higher_tax'], ['strongly disagree', 'disagree', 'neutral', 'agree', 'strongly agree'], ordered=True)
# print(census['higher_tax'].unique())

# Find the higher_tax median
# Convert categorical data to numerical data
census['higher_tax'] = census['higher_tax'].cat.codes
# print(census['higher_tax'].unique())
median_higher_tax = census['higher_tax'].median()
print(f"The median of higher tax is {median_higher_tax}")

# Label Encoding the marital_status column
census['marital_status_code'] = pd.Categorical(census['marital_status'], ['single', 'divorced', 'married', 'widowed'], ordered=True)

census['marital_status_code'] = census['marital_status_code'].cat.codes
# print(census['marital_status_code'].unique())

# Create One-Hot Encode for marital_status column
census = pd.get_dummies(data=census, columns=['marital_status'])
# print(census.head(5))
# print(census.dtypes)

# Create new column age
current_year = 2024
census['age'] = current_year - census['birth_year']

# Create bins and labels
bins = [0, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
labels = ['0-25', '26-30', '31-35', '36-40', '41-45', '46-50', '51-55', '56-60', '61-65', '66-70', '71-75', '76-80', '81-85', '86-90', '91-95', '96-100']

# Create age_group the age_group column
census['age_group'] = pd.cut(census['age'], bins=bins, labels=labels, right=True)
#print(census.head(5))

# Label Encoding
# print(census['age_group'].unique())
census['age_group_code'] = census['age_group'].cat.codes
print(census.head(5))