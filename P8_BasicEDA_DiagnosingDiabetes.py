import pandas as pd
import numpy as np

# Load data
diabetes_data = pd.read_csv('data/diabetes.csv')
print(diabetes_data.head(5))

# Check rows and columns
print(diabetes_data.columns)
print(len(diabetes_data))
## Index(['Pregnancies', 'Glucose','BloodPressure', 'SkinThickness', 'Insulin','BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome'],dtype='object')
## 768 rows

# Check missing value
print(diabetes_data.isnull().sum())
# print(diabetes_data.info())
# print(diabetes_data.describe())
print("The minimum value for columns Glucose, BloodPressure, SkinThickness, Insulin, BMI are all 0. These are missing values in the data.")
print("The maximum value of the Insulin column is 846, which is abnormally high")
print("The maximum value of the Pregnancies column is 17. While having 17 pregnancies is not impossible, this case might be something to look further into to determine its accuracy")

# replace 0 with NaN in 5 columns to get more accurate view of the missing values in the data
diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0, np.nan)

# check for missing values
print(diabetes_data.isnull().sum())
# print(diabetes_data.info())

# print out the rows with missing values
print(diabetes_data[diabetes_data.isnull().any(axis=1)])
print("most rows with missing data have missing values in more than one column. In fact, every single row with at least one missing value also has a missing value in the Isulin column.")
print("Choose to remove specific rows or impute the missing values with mean, median, or mode")

# Check data types
print(diabetes_data.dtypes)
print("The Outcome column is of type object, expected int64")

# Check Outcome column
print(diabetes_data['Outcome'].unique())
# ['1' '0' 'O']

# replace 'O' with '0' and convert Outcome to int64
diabetes_data['Outcome'] = diabetes_data['Outcome'].replace('O', '0')
diabetes_data['Outcome'] = diabetes_data['Outcome'].astype('int64')
# print(diabetes_data['Outcome'].unique())


