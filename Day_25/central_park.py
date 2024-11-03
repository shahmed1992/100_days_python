"""
1. Create a final csv file using the data present in 2018_Central_Park...  csv file
2. final csv file should look like following(squirrel_count.csv):
    a.Fur Color, Count

"""


import pandas
from  collections import Counter

def my_approach():
    raw_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20241103.csv")
    list_fur_color = raw_data["Primary Fur Color"].to_list()
    list_fur_color = [x for x in list_fur_color if type(x)!=float]

    res_dict = dict(Counter(list_fur_color))
    res_dict1 = {"Fur Color": res_dict.keys(), "Count": res_dict.values()}

    df_data = pandas.DataFrame(res_dict1)
    df_data.to_csv("squirrel_count.csv")

def mentor_approach():
    data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20241103.csv")
    gray_squirrels_count = len(data[data["Primary Fur Color"]=="Gray"])
    red_squirrels_count = len(data[data["Primary Fur Color"]=="Cinnamon"])
    black_squirrels_count = len(data[data["Primary Fur Color"]=="Black"])
    data_dict = {
        "Fur Color":["Gray","Red","Black"],
        "Count":[gray_squirrels_count, red_squirrels_count, black_squirrels_count]
    }

    df_data = pandas.DataFrame(data_dict)
    df_data.to_csv("squirrel_count_2.csv")



mentor_approach()