# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}
def updated_damage(damages, conversion):
  damage_new_list = []
  for damage in damages:
    if "M" in damage:
      clean_damage = damage.replace("M", "")
      float_damage = float(clean_damage)
      convert_damage = conversion["M"] * float_damage
      damage_new_list.append(convert_damage)
    elif "B" in damage:
      clean_damage = damage.replace("B", "")
      float_damage = float(clean_damage)
      convert_damage = conversion["B"] * float_damage
      damage_new_list.append(convert_damage)
    else:
      damage_new_list.append(damage)
  return damage_new_list

# test function by updating damages
test_damages_list = updated_damage(damages, conversion)
#print(test_damages_list)

# 2 
# Create a Table
def create_hurricanes_table(names, months, years, max_sustained_winds, areas_affected, damages_updated, deaths):
  hurricanes = {}
  for index in range(len(names)):
    hurricanes[names[index]] = {
      "Name": names[index],
      "Month": months[index],
      "Year": years[index],
      "Max Sustained Wind": max_sustained_winds[index],
      "Areas Affected": areas_affected[index],
      "Damage": damages_updated[index],
      "Deaths": deaths[index]
      }
  return hurricanes

# Create and view the hurricanes dictionary
test_hurricanes = create_hurricanes_table(names, months, years, max_sustained_winds, areas_affected, test_damages_list, deaths)

#print(test_hurricanes)

# 3
# Organizing by Year
def year_hurricanes(hurricanes_table):
  hurricanes_by_years = {}

  for hurricane in hurricanes_table.values():
    year = hurricane["Year"]
    if year not in hurricanes_by_years:
      hurricanes_by_years[year] = []
    hurricanes_by_years[year].append(hurricane)

  return hurricanes_by_years
# create a new dictionary of hurricanes with year and key
test_year_hurricane = year_hurricanes(test_hurricanes)
#print(test_year_hurricane[1932])

# 4
# Counting Damaged Areas
def area_count_hurricanes(hurricanes_table):
    hurricanes_count_by_areas = {}

    for hurricane in hurricanes_table.values():
        areas = hurricane["Areas Affected"]
        for area in areas:
            if area in hurricanes_count_by_areas:
                hurricanes_count_by_areas[area] += 1  
            else:
                hurricanes_count_by_areas[area] = 1

    return hurricanes_count_by_areas
# create dictionary of areas to store the number of hurricanes involved in
test_area_count = area_count_hurricanes(test_hurricanes)
#print(test_area_count)

# 5 
# Calculating Maximum Hurricane Count
def max_hurricane(hurricanes_table):
  max_num = 0
  for value in hurricanes_table.values():
    if value > max_num:
      max_num = value
  return max_num

# find most frequently affected area and the number of hurricanes involved in
test_max = max_hurricane(test_area_count)
#print(test_max)

# 6
# Calculating the Deadliest Hurricane
def name_and_death(names, deaths):
  n_d_dict = {}
  for i in range(len(names)):
    n_d_dict[names[i]] = deaths[i]
  return n_d_dict

def find_max_death(table):
  area_max = ''
  max_death = 0
  for name, death in table.items():
    if death > max_death:
      max_death = death
      area_max = name
  return area_max, max_death

# find highest mortality hurricane and the number of deaths
test_name_death = name_and_death(names, deaths)
#print(test_name_death)

max_mortality_cane, max_mortality = find_max_death(test_name_death)
#print(f"The hurricane with the highest mortality is {max_mortality_cane} with {max_mortality} deaths.")

# 7
# Rating Hurricanes by Mortality
def rating_hurricanes(hurricane_data):
  hurricanes_by_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for name_index, data in hurricane_data.items():
    if data['Deaths'] > 10000:
      hurricanes_by_mortality[5].append(data)
    elif data['Deaths'] > 1000:
      hurricanes_by_mortality[4].append(data)
    elif data['Deaths'] > 500:
      hurricanes_by_mortality[3].append(data)
    elif data['Deaths'] > 100:
      hurricanes_by_mortality[2].append(data)
    elif data['Deaths'] > 0:
      hurricanes_by_mortality[1].append(data)
    else:
      hurricanes_by_mortality[0].append(data)
  return hurricanes_by_mortality

# categorize hurricanes in new dictionary with mortality severity as key
rating_hur = rating_hurricanes(test_hurricanes)
#print(rating_hur[4])

# 8 Calculating Hurricane Maximum Damage
def name_and_damage(names, damages_list):
  n_d_dict = {}
  for i in range(len(names)):
    n_d_dict[names[i]] = damages_list[i]
  return n_d_dict

def find_max_damage(data):
  area_max_damage = ''
  max_damage = 0
  total_damage = 0

  for name, damage in data.items():
    if isinstance(damage, str):
      continue
    elif isinstance(damage, (float, int)):
      total_damage += damage
      if damage > max_damage:
        max_damage = damage
        area_max_damage = name
  return area_max_damage, max_damage, total_damage
# find highest damage inducing hurricane and its total cost
test_data = name_and_damage(names, test_damages_list)
area_max_damage, max_damage, total_damage = find_max_damage(test_data)
#print(f"Highest damage: {area_max_damage} with USD {max_damage:,.2f}. Total damage: USD {total_damage:,.2f}.")

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
def rating_dam_hurricanes(hurricane_data):
  hurricanes_by_damage = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for name_index, data in hurricane_data.items():
    if isinstance(data['Damage'], str):
      hurricanes_by_damage[0].append(data)
    elif isinstance(data['Damage'], (float, int)):
      if data['Damage'] > 50000000000:
        hurricanes_by_damage[5].append(data)
      elif data['Damage'] > 10000000000:
        hurricanes_by_damage[4].append(data)
      elif data['Damage'] > 1000000000:
        hurricanes_by_damage[3].append(data)
      elif data['Damage'] > 100000000:
        hurricanes_by_damage[2].append(data)
      elif data['Damage'] > 0:
        hurricanes_by_damage[1].append(data)
      else:
        hurricanes_by_damage[0].append(data)
  return hurricanes_by_damage  


# categorize hurricanes in new dictionary with damage severity as key
rating_dam_hur = rating_dam_hurricanes(test_hurricanes)
print(rating_dam_hur[0])
