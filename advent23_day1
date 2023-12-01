import pandas as pd
import numpy as np
import re



##################
#     Part 1     #
##################

# read in data text file - assign all strings to "raw_string" column
input = pd.read_csv("advent_day1_input1.txt", sep=" ", header=None, names=["raw_string"])

# create column of all the digits in raw_string column
input["all_numeric"] = input["raw_string"].str.findall(r"\d+(?:\.\d+)?").str.join("")

# create new column "first" that is the first number in the string
input["first"] = input["all_numeric"].str[0]

# create new column "last" that is the last number in the string
input["last"] = input["all_numeric"].str[-1]

# concatenate columns "first" and "last" and change type to integer
input["first_and_last"] = (input["first"] + input["last"]).astype("int")

# sum two digit column "first_and_last"
part1_sum = input["first_and_last"].sum()

# print Part 1 answer
print("Part 1 Sum = ", part1_sum)



##################
#     Part 2     #
##################

# list of all values that equal a numeric value including words 
list_of_numbers = ["one", "two", "three", "four", "five", "six", "seven", 
                   "eight", "nine", "zero", "1", "2", "3", "4", "5", "6", 
                   "7", "8", "9", "0"]

# list with all numeric words spelled backwards
numbers_reverse = ["eno", "owt", "eerht", "ruof", "evif", "xis", "neves", 
                   "thgie", "enin", "orez", "1", "2", "3", "4", "5", "6", 
                   "7", "8", "9", "0"]

# join "list_of_numbers" with | to use in regex "findall" function later
join_number = "|".join(x for x in list_of_numbers) 

# join "numbers_reverse" with | to use in regex "findall" function later
join_reverse = "|".join(x for x in numbers_reverse)

# add "\b" to start and finish is joined lists above
re_string = f"\bjoin_number\b"
reverse_str= f"\bjoin_reverse\b"

# use re(gex)_string to use in "findall" function. Join items by comma
input["get_words"] = input["raw_string"].str.findall(join_number).str.join(",").str.lower()

# flip raw_string to show reverse order (read backwards)
input["intermed_reverse"] = input["raw_string"].apply(lambda x: x[::-1])

# use reverse_str to use in "findall" function. Join items by comma
input["get_reverse"] = input["intermed_reverse"].str.findall(join_reverse).str.join(",").str.lower()

# "new_first" and "new_last" by partitioning list above by comma and keeping 
# first value (first value of "new_last" is the last value of "get_words", 
# but since in reverse order than the first is needed)
input["new_first"] = input["get_words"].str.partition(",")[0]
input["new_last"] = input["get_reverse"].str.partition(",")[0]

# create dictionaries to convert words to numbers using key:value pairs
number_dict = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", 
               "seven":"7", "eight":"8", "nine":"9", "zero":"0"}

reverse_dict = {"eno":"1", "owt":"2", "eerht":"3", "ruof":"4", "evif":"5", "xis":"6", 
               "neves":"7", "thgie":"8", "enin":"9", "orez":"0"}

# Creating copies to verify the replace function works correctly. This step is not necessary
input["final_first"] = input["new_first"]
input["final_last"]  = input["new_last"]

# replace all values in "final_first" and "final_last" by matching key to value 
# in respective dictionaries
input["final_first"].replace(number_dict, inplace=True)
input["final_last"].replace(reverse_dict, inplace=True)

# concatenate "final_first" value with "final_last" value 
# change type to integer (2 digit number) 
input["final_first_and_last"] = (input["final_first"] + input["final_last"]).astype("int")

# sum "final_first_and_last" for Part 2 answer
part2_sum = input["final_first_and_last"].sum()

# create cumulative_sum column to verify sum step is working correctly. 
# This step is not necessary
input["cumulative_sum"] = input["final_first_and_last"].cumsum()

# print Part 2 answer
print("Part 2 Sum = ", part2_sum)
