# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         print(row)
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)
print(len(temp_list))

# total = sum(temp_list) / len(temp_list)
# print(total)

print(data["temp"].mean())
print(data["temp"].max())

# collumn
print(data["condition"])
print(data.condition)

# row
print(data[data["day"] == "Monday"])
print(data[data["temp"] == data["temp"].max()])

# Convert to Fahrenheit
monday = data[data.day == "Monday"]
# print(monday.condition)
monday_temp = monday.temp[0]
monday_temp_F = monday.temp * 9/5 + 32

print(monday_temp_F)


# Create a Dataframe
data_dict = {
    "students": ["James", "John", "Amaro"],
    "scores": [76, 56, 99]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
