import pandas as pd

# Load data from the 'data' folder
visits = pd.read_csv('data/visits.csv', parse_dates=[1])
cart = pd.read_csv('data/cart.csv', parse_dates=[1])
checkout = pd.read_csv('data/checkout.csv', parse_dates=[1])
purchase = pd.read_csv('data/purchase.csv', parse_dates=[1])

# Task 2: Left merge visits and cart
visits_cart_merged = pd.merge(visits, cart, how='left')

# Task 4: Number of null for the cart_time column
null_cart_times = visits_cart_merged[visits_cart_merged.cart_time.isnull()]
num_null_cart_times = len(null_cart_times)

# Task 5: Cart Abandonment Rate
percent_no_cart = float(num_null_cart_times) / len(visits_cart_merged) * 100
print(f"Cart Abandonment Rate: {percent_no_cart:.2f}%")

# Task 6: Left merge cart and checkout
cart_checkout_merged = pd.merge(cart, checkout, how='left')
num_null_checkout_time = len(cart_checkout_merged[cart_checkout_merged.checkout_time.isnull()])

# Checkout Abandonment Rate
percent_no_checkout = float(num_null_checkout_time) / len(cart_checkout_merged) * 100
print(f"Checkout Abandonment Rate: {percent_no_checkout:.2f}%")

# Task 7: Merge all four DataFrames
all_data = visits.merge(cart, how='left').merge(checkout, how='left').merge(purchase, how='left')
## print(all_data.head(5))

# Task 8: Purchase Abandonment Rate
num_checkout = len(all_data[all_data.checkout_time.notnull()])
num_null_purchase_time = len(all_data[(all_data.purchase_time.isnull()) & (all_data.checkout_time.notnull())])
percent_no_purchase = float(num_null_purchase_time) / num_checkout * 100
print(f"Purchase Abandonment Rate: {percent_no_purchase:.2f}%")

# Task 9: Summary statement
print("")
print(f"The weakest step in the funnel is the cart stage, with a cart abandonment rate of {percent_no_cart:.2f}%. Cool T-Shirts Inc. could improve this by simplifying navigation, offering promotions, and enhancing product information to encourage users to add items to their cart.")

# Task 10: Average Time to Purchase
all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time
## print(all_data.time_to_purchase)

# Task 12: Calculate the average time to purchase
average_time_to_purchase = all_data['time_to_purchase'].mean()
print("")
print(f"""The average time from initial visit to final purchase is {average_time_to_purchase}.
This metric helps Cool T-Shirts Inc. understand the typical duration of the customer journey
from visiting the website to completing a purchase.""")
