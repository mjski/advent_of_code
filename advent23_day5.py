import pandas as pd
import numpy as np

##################
#     Part 1     #
##################

name_list = ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 
            'water-to-light', 'light-to-temperature', 'temperature-to-humidity',
            'humidity-to-location']


# read in data text file
input = pd.read_csv(r"H:\Scripts\advent_of_code\2023\advent_day5_test_input.txt", header=None)

seeds = []
tmp = input.iloc[0,0]
tolst = tmp.replace("seeds: ", "").strip()
seeds = [int(s) for s in tolst.split(" ")]
# print(seeds)

input.drop(0, axis=0, inplace=True)
# print(input)
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

        sub_df = pd.concat([sub_df, tmp_df], axis = 1)        # sub_df.iloc[:,k] = d.iloc[1:, 0].reset_index()
        # print(d.iloc[1:, 0]) #.reset_index().drop('index', inplace=True))
    return sub_df

sub_df = create_df()
sub_df.columns = name_list
print(len(sub_df.columns))

for seed in seeds:
    for row, col in sub_df.items():
        print(seed)
# print(sub_df)




