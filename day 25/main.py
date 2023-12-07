import csv
import pandas
with open("./002 weather-data.csv") as data_file:
    weather_data = csv.reader(data_file)
    temperature =[]
    for row in weather_data:
        if row[1]== 'temp':
            temperature.append(row[1])
        else:
            temperature.append(int(row[1]))

print(temperature)