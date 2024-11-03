
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
import pandas # https://pandas.pydata.org/docs/user_guide/index.html#user-guide
# https://docs.google.com/spreadsheets/d/1Rs1CKjiagTeXa53212JkjRSDu-tx77_YxEgGdkv5zRY/edit?gid=0#gid=0

def excel_data_using_pandas():
    data = pandas.read_csv("weather_data.csv")
    # print(data) # prints full table
    # print(data["temp"]) # prints temp column also called as series
    # print(type(data))

    data_dict = data.to_dict()  # converting the data to dictionary
    # print(data_dict)

    temp_list = data["temp"].to_list() # converting the temp column to a list
    # print(temp_list)

    avg_temp = sum(temp_list) / len(temp_list) # Calculating the avg of temperatures.
    # print(f"{avg_temp = }")

    avg_temp2 = data["temp"].mean()
    # print(avg_temp2)

    max_temp = int(data["temp"].max())
    # print(f"{max_temp = }")

    # Alternative to square bracket
    # print(data["condition"])
    # print(data.condition)

    # Get data in row
    monday_data = data[data.day == "Monday"]
    # print(monday_data)

    # Get row data where the temp was max
    max_temp_data = data[data.temp == max_temp]
    # print(max_temp_data)

    # Converting monday's temp to fahrenheit
    fahrenheit_temp_monday = monday_data.temp * 9/5 +32
    # print(fahrenheit_temp_monday)

    # Create Dataframe from scratch
    student_data_dict = {
        "students": ["Amy", "James", "Angela"],
        "scores": [76, 56, 65]
    }
    df_data = pandas.DataFrame(student_data_dict)
    df_data.to_csv("student_data")
    # print(df_data)
excel_data_using_pandas()
