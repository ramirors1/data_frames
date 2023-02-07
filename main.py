

#with open("weather.data.csv") as data_file:
#    data = data_file.readlines()
#    print(data)

#import csv

#with open("weather.data.csv") as data_file:
 #   data = csv.reader(data_file)
  #  temperatures = []
   # for row in data:
        #print(row[1])  # will print temperatures including the temp label
    #    if row[1] != "temp":  #this if statement and code below will only print the temperatures, not the temp label
     #       temperatures.append(int(row[1]))
    #print(temperatures)

# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# #print(data["temp"])
#
# data_dict = data.to_dict()  #converst data to a Python dictionary
# print(data_dict)
#
# temp_list = data["temp"].to_list() # converts data to a Python list
# print(temp_list)
#
# #average = sum(temp_list) / len(temp_list)
# #print(average)
#
# #print(data["temp"].mean())  #shorter than above way to get the average temps
# print(data["temp"].max())  #gets the max of a list
#
# #getting a row of data
# print(data[data.day == "Monday"])
#
# #gets the row with the highest temp
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# #print(monday.condition)
#
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32  #converts celsius to Farenheit
# print(monday_temp_F)

#create dataframe
#data_dict = {
#    "students": ["Amy", "James", "Angela"],
#    "scores": [76, 56, 65]
#}
#new_data = pandas.DataFrame(data_dict)
#data.to_csv("new_data.csv") # creates new csv file

import pandas

data = pandas.read_csv("squirrel_data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {  #converst data to a Python dictionary
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

dframe = pandas.DataFrame(data_dict)
dframe.to_csv("squirrel_count.csv") # creates new csv file