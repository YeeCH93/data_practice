import pandas as pd

# 1 examine the data
ad_clicks = pd.read_csv('ad_clicks.csv')
#print(ad_clicks.head())

# 2 platform with most views
view_by_source = ad_clicks.groupby('utm_source').user_id.count().reset_index()
#print(view_by_source)

# 3 create Boolean column
ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()

# 4 number of clicks by utm_source
clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()
#print(clicks_by_source)

# 5 show in pivot table format
clicks_pivot = clicks_by_source.pivot(
  columns='is_click',
  index='utm_source',
  values='user_id'
).reset_index()

# 6 percentage of click by utm_source
clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])
#print(clicks_pivot)

# 7 Check user distribution between Ad A and Ad B
exp_group_count = ad_clicks.groupby('experimental_group').user_id.count().reset_index()
#print(exp_group_count)

# 8 Compare click rates for Ad A and Ad B
click_per_exp = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()
#print(click_per_exp)
click_per_exp_pivot = click_per_exp.pivot(
  columns='is_click',
  index='experimental_group',
  values='user_id'
).reset_index()

click_per_exp_pivot['percentage_click'] = click_per_exp_pivot[True] / (click_per_exp_pivot[True] + click_per_exp_pivot[False])
#print(click_per_exp_pivot)

# 9 Create DataFrames for Ad A and Ad B
a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']

# 10 Calculate daily click rates for Ad A and Ad B
a_group = a_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()
#print(a_group)

a_group_pivot = a_group.pivot(
  columns='is_click',
  index='day',
  values='user_id'
).reset_index()
#print(a_group_pivot)

a_group_pivot['a_percentage'] = (a_group_pivot[True] / (a_group_pivot[True] + a_group_pivot[False])).round(2)
#print(a_group_pivot)

# b
b_group = b_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()

b_group_pivot = b_group.pivot(
  columns='is_click',
  index='day',
  values='user_id'
).reset_index()

b_group_pivot['b_percentage'] = (b_group_pivot[True] / (b_group_pivot[True] + b_group_pivot[False])).round(2)
#print(b_group_pivot)

# 11 Compare daily click rates and recommend ad
a_clicks_summary = a_group_pivot[['day', 'a_percentage']]
b_clicks_summary = b_group_pivot[['day', 'b_percentage']]
comparison_table = pd.merge(a_clicks_summary, b_clicks_summary, on='day')
comparison_table['diff_a_b'] = (comparison_table['a_percentage'] - comparison_table['b_percentage']).round(2)
print(comparison_table)
print(f"Based on the data, Ad A has higher click rates on most days. It is recommended to use Ad A.")