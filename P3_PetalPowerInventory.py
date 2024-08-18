import pandas as pd

# load data
inventory = pd.read_csv('inventory.csv')

# inspect first 10 rows
#print(inventory.head(10))

# select location = Staten Island
staten_island = inventory[inventory['location'] == 'Staten Island']
#print(staten_island)

# select product_description from Staten Island
product_request = staten_island['product_description']
#print(product_request)

# what types of seeds are sold at the Brooklyn location
seed_request = inventory[(inventory['location'] == 'Brooklyn') & (inventory['product_type'] == 'seeds')]
#print(seed_request)

# add new column to check inventory quantity
inventory['in_stock'] = inventory.apply(lambda row: True if row.quantity > 0 else False, axis=1)
#print(inventory)

# add column total_value
inventory['total_value'] = inventory.price * inventory.quantity
#print(inventory)

# add column full_description
combine_lambda = (lambda row: f'{row.product_type} - {row.product_description}')

inventory['full_description'] = inventory.apply(combine_lambda, axis=1)
print(inventory)

