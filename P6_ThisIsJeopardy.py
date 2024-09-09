import pandas as pd
#pd.set_option('display.max_colwidth', -1)

# Load the dataset
jeopardy = pd.read_csv('data/jeopardy.csv')
# print(jeopardy.columns) 
## space at the front of the column name
# print(jeopardy.info()) 
## non-null

# Clean column names by stripping leading/trailing spaces
jeopardy.columns = jeopardy.columns.str.strip()
# print(jeopardy.columns)

# Function to filter questions containing all words in a list
def filter_question(data, words):
  filter_func = lambda x: all(word.lower() in x.lower() for word in words)
  return data[data['Question'].apply(filter_func)]

# Test the filter_question function
filtered_data = filter_question(jeopardy, ["King", "England"])
print(f"This function return {len(filtered_data)} rows") 
## 152 rows
# print(filtered_data['Question'])

# Compute average on the Value column
# Lambda function to clean the 'Value' column
clean_num = (lambda x: float(x.replace('$','').replace(',','')) if x != 'no value' else 0)
# Apply the clean_value function to the 'Value' column
jeopardy['Float Value'] = jeopardy['Value'].apply(clean_num)

# Compute average value for questions containing 'King'
filter_king_data = filter_question(jeopardy, ['King'])
avg_val_king_q = filter_king_data['Float Value'].mean()
print(f"For question that contain word 'King', the average value is ${avg_val_king_q:.2f}")

# Function to count unique answers
def count_unique_answers(data):
  return data['Answer'].value_counts()

# Test the count_unique_answers function
unique_answers = count_unique_answers(filter_king_data)
top_n = 10
print(f"Top {top_n} unique answer are \n{unique_answers.head(top_n)}")
