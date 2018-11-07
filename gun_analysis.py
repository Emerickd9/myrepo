import csv
import datetime

#reading in csv file using csv module
with open("full_data.csv","r") as file:
    data = list(csv.reader(file))[1:] #taking only the data leaving the headers
    headers = list(csv.reader(file))[:1] #here are the headers

#list comprehension to get a list of years from the year column
years = [row[1] for row in data]

year_counts = {}

#counting the number of death occurence in the occurencce of any year mentioned in the data
for year in years:
    if year in year_counts:
        year_counts[year] = year_counts[year] + 1
    else:
        year_counts[year] = 1

#print(year_counts)

dates = [datetime.datetime(int(row[1]), int(row[2]), 1) for row in data]
#print(dates[5:])

date_counts = {}
for date in dates:
    if date in date_counts:
        date_counts[date] = date_counts[date] + 1
    else:
        date_counts[date] = 1

for ind, value in date_counts.items():
    print(ind,":->", value)


sex = [row[5] for row in data]
gender_counts = {}

for gender in sex:
    if gender in gender_counts:
        gender_counts[gender] = gender_counts[gender] +  1
    else:
        gender_counts[gender] = 1
for ind, value in gender_counts.items():
    print(ind,":->", value)

races = [row[7] for row in data]
race_counts = {}

for race in races:
    if race in race_counts:
        race_counts[race] = race_counts[race] +  1
    else:
        race_counts[race] = 1
for ind, value in race_counts.items():
    print(ind,":->", value)

#Answer to the question in information document

intents = [row[3] for row in data]
homicide_race_counts = {}
for i,race in enumerate(races):
    if race not in homicide_race_counts:
        homicide_race_counts[race] = 0
    if intents[i] == "Homicide":
        homicide_race_counts[race] += 1

race_per_hundredk = {}
for k,v in homicide_race_counts.items():
    race_per_hundredk[k] = (v / mapping[k]) * 100000

race_per_hundredk