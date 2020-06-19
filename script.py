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

# write your update damages function here:
def function1(lst):
    temp_list = []
    M = 10**6
    B = 10**9
    for data in lst:
        try:
            if int(data[0]) * 0 == 0:
               if "M" in data:
                   data = data.strip("M")
                   data = float(data) * M
                   temp_list.append(data)
               else:
                   data = data.strip("B")
                   data = float(data) * B
                   temp_list.append(data)
        except:
            temp_list.append(data)
    return temp_list
#print(function1(damages))


def function2(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    dict1 = {}
    damages = function1(damages)
    for times in range(len(names)):
        dict1.update({names[times]: {"Name": names[times], "Month": months[times], "Year": years[0], "Max_Sustained_Wind": max_sustained_winds[times], "Areas_Affected": areas_affected[times], "Damage": damages[times], "Deaths": deaths[times]}})
    return dict1
#print(function2(names,months, years, max_sustained_winds, areas_affected, damages, deaths))


def function3(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    dict1 = {}
    damages = function1(damages)
    for times in range(len(years)):
        dict1.update({years[times]: {"Name": names[times], "Month": months[times], "Year": years[0], "Max_Sustained_Wind": max_sustained_winds[times], "Areas_Affected": areas_affected[times], "Damage": damages[times], "Deaths": deaths[times]}})
    return dict1
#print(function3(names, months, years, max_sustained_winds, areas_affected, damages, deaths))


def function4(areas_affected):
    dict1 = {}
    areas = []
    mixed = []
    for i in areas_affected:
        for area in i:
            mixed.append(area)
            if area not in areas:
                areas.append(area)
    for area in areas:
        dict1[area] = mixed.count(area)
    return dict1
#print(function4(areas_affected))


def function5(areas_affected):
    dict1 = function4(areas_affected)
    dict2 = {}
    max_value = (max(dict1.values()),)
    while len(max_value) > 0 and max_value[-1] in list(dict1.values()):
          index_of_value = list(dict1.values()).index(max_value[-1])
          corresponding_area = list(dict1.keys())[index_of_value]
          dict2[corresponding_area] = dict1.pop(corresponding_area)
    return dict2
#print(function5(areas_affected))


def function6(deaths, names):
    dict1 = {names: deaths for (names, deaths) in zip(names,deaths)}
    dict2 = {}
    max_death = (max(dict1.values()),)
    while len(max_death) > 0 and max_death[-1] in list(dict1.values()):
          index_of_max_death = list(dict1.values()).index(max_death[-1])
          corresponding_huricane = list(dict1.keys())[index_of_max_death]
          dict2[corresponding_huricane] = dict1.pop(corresponding_huricane)
    return dict2
#print(function6(deaths, names))


def function7(deaths, names):
    dict1 = {}
    for num in range(6):
        dict1[num] = []
    for death, names in zip(deaths, names):
        if death > 10000:
           dict1[5] = [name for name in dict1.get(5)] + [names]
        elif death > 1000:
           dict1[4] = [name for name in dict1.get(4)] + [names]
        elif death > 500:
           dict1[3] = [name for name in dict1.get(3)] + [names]
        elif death > 100:
           dict1[2] = [name for name in dict1.get(2)] + [names]
        elif death > 0:
           dict1[1] = [name for name in dict1.get(1)] + [names]
        else:
           dict1[0] = [name for name in dict1.get(0)] + [names]
    return dict1
#print(function7(deaths, names))


def function8(names, damages):
    dict1 = {}
    damages = function1(damages)
    print(damages)
    for damage in damages:
        if damage * 0 == 0:
           damages1.append(damage)
        else:
            damages1.append(0)
    max_damage = max(damages1)
    for damage, name in zip(damages1, names):
        if damage == max_damage:
           dict1[name] = damage
    return dict1
#print(function8(names, damages))


def function9(names ,damages):
    dict1 = {}
    damages1 = []
    damages = function1(damages)
    def inbuiltfun(damages):
        lst = []
        for damage in damages:
            if damage * 0 == 0:
               lst.append(damage)
            else:
                lst.append(0)
        return lst
    damages = inbuiltfun(damages)
    for num in range(6):
        dict1[num] = []
    for damage, name in zip(damages, names):
        if damage > 50000000000:
           dict1[5] = [name for name in dict1.get(5)] + [name]
        elif damage > 10000000000:
           dict1[4] = [name for name in dict1.get(4)] + [name]
        elif damage > 1000000000:
           dict1[3] = [name for name in dict1.get(3)] + [name]
        elif damage > 100000000:
           dict1[2] = [name for name in dict1.get(2)] + [name]
        elif damage > 0:
           dict1[1] = [name for name in dict1.get(1)] + [name]
        else:
           dict1[0] = [name for name in dict1.get(0)] + [name]
    return dict1
print(function9(names, damages))
























