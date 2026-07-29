# import csv
#
# with open("weather_data.csv") as data_file:
#     reader = csv.reader(data_file)
#     headline = next(reader)
#
#     temperatures = []
#     for row in reader:
#         temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

data = pandas.read_csv("./weather_data.csv")
temp_list = data["temp"].tolist()

# Get Data in Row
print(data[data.day == "Monday"])

# Get the row with the highest temperature
print(data[data.temp == data.temp.max()])

# Convert Monday's temperature to Fahrenheit
monday = data[data.day == "Monday"]
fahrenheit = monday.temp * 9 / 5 + 32
# print(fahrenheit)

# Create a Dataframe from scratch
data_dict = {
    "students": ["Ana", "David", "Loren"],
    "scores": [9, 7, 10]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")