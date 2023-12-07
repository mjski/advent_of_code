import pandas as pd
import numpy as np

##################
#     Part 1     #
##################

name_list = ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 
            'water-to-light', 'light-to-temperature', 'temperature-to-humidity',
            'humidity-to-location']


# read in data text file
input = pd.read_csv(r"H:\Scripts\advent_of_code\2023\advent_day5_input.txt", header=None)

seeds = []
tmp = input.iloc[0,0]
tolst = tmp.replace("seeds: ", "").strip()
seeds = [int(s) for s in tolst.split(" ")]

input.drop(0, axis=0, inplace=True)
part1 = pd.DataFrame()

def create_df():
    sub_df = pd.DataFrame()
    for k, d in input.groupby(input[0].str.endswith('map:').fillna(0).cumsum()):
        tmp_df = pd.DataFrame()
        column_name = str(d.iloc[0,0])
        data = d.iloc[1:, 0]
        tmp_df.loc[:, column_name] = data
        
        tmp_df.reset_index(inplace=True)
        tmp_df.drop("index", axis=1, inplace=True)

        sub_df = pd.concat([sub_df, tmp_df], axis = 1)
    return sub_df

sub_df = create_df()
sub_df.fillna("-1 -1 -1", inplace=True)
sub_df.columns = name_list
sub_df = sub_df.loc[:, :].replace(' ', ', ', regex = True)

dest_cols = ['soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']
# dest_dict = {key:[] for key in seeds}


def get_map_value(source_col):
    for seed in seeds:
        for idx, col in sub_df[source_col].items():    
            row_dest = int(col.split(',')[0])
            row_source = int(col.split(',')[1])
            row_range = int(col.split(',')[2])
            if int(seed) in range(row_source, row_source + row_range):
                diff = int(seed) - row_source
                dest_val = row_dest + diff
                dest_dict[seed].append(dest_val)
        if dest_dict[seed] == []:
            dest_dict[seed].append(seed)
    return dest_dict


# seed_to_soil_dict = get_map_value("seed-to-soil")
# print(seed_to_soil_dict)


def get_map_value(source_col, source_list):
    dest_dict = {key:[] for key in source_list}
    for seed in source_list:
        for idx, col in sub_df[source_col].items():    
            row_dest = int(col.split(',')[0])
            row_source = int(col.split(',')[1])
            row_range = int(col.split(',')[2])
            if int(seed) in range(row_source, row_source + row_range):
                diff = int(seed) - row_source
                dest_val = row_dest + diff
                dest_dict[seed].append(dest_val)
        if dest_dict[seed] == []:
            dest_dict[seed].append(seed)
    return dest_dict


seed_to_soil_dict = get_map_value("seed-to-soil", seeds)
# soil_list = []
soil_list = [val for lst in seed_to_soil_dict.values() for val in lst]
# print("soil:", soil_list)

soil_to_fertilizer_dict = get_map_value("soil-to-fertilizer", soil_list)
fertilizer_list =  [val for lst in soil_to_fertilizer_dict.values() for val in lst]
# print('fertilizer:', fertilizer_list)

fertilizer_to_water_dict = get_map_value("fertilizer-to-water", fertilizer_list)
water_list =  [val for lst in fertilizer_to_water_dict.values() for val in lst]
# print('water:', water_list)

water_to_light_dict = get_map_value("water-to-light", water_list)
light_list =  [val for lst in water_to_light_dict.values() for val in lst]
# print('light:', light_list)

light_to_temperature_dict = get_map_value("light-to-temperature", light_list)
temperature_list =  [val for lst in light_to_temperature_dict.values() for val in lst]
# print('temperature:',temperature_list)

temperature_to_humidity_dict = get_map_value("temperature-to-humidity", temperature_list)
humidity_list =  [val for lst in temperature_to_humidity_dict.values() for val in lst]
# print('humidity:', humidity_list)

humidity_to_location_dict = get_map_value("humidity-to-location", humidity_list)
location_list =  [val for lst in humidity_to_location_dict.values() for val in lst]
# print('location:', location_list)

print("lowest_location:", sorted(location_list)[0])


##################
#     Part 2     #
##################



