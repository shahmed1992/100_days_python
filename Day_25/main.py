
""" Using csv library"""
import csv
def excel_data_using_csv():
    with open("weather_data.csv") as weather_data:
        csv_reader = csv.reader(weather_data)
        # data = weather_data.readlines()
        # print(csv_reader)
        temperatures = []
        for index,row in enumerate(csv_reader):
            # print(row)
            if index == 0:
                continue
            temperatures.append(int(row[1]))
        print(temperatures)

"""Using pandas library"""
import pandas

def excel_data_using_pandas():
    data = pandas.read_csv("weather_data.csv")
    print(data)

excel_data_using_pandas()
