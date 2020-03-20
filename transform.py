import csv
import os
import dateparser

path = r'csse_covid_19_data/csse_covid_19_daily_reports/'

def get_data(f, countries):
    result = []
    target_positions = [3, 4, 5]
    target_names = ['','','','Confirmed', 'Deaths', 'Recovered']
    province_position = 0
    country_position = 1    

    with open(os.path.join(path, f)) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        
        for row in reader:
            # apply filter
            if row[country_position] not in countries: continue

            # get rid of cities
            if ',' in row[province_position] or row[province_position] == 'Chicago': continue

            date = dateparser.parse(f.split('.')[0])
            for target in target_positions:
                count = row[target] or '0'
                result.append([f'"{row[0]}"', f'"{row[1]}"', str(date).split(' ')[0], target_names[target], count])
    
    return result

files = [f for f in os.listdir(path) if f.split('.')[1] == 'csv']

print('Province/State,Country/Region,Date,Metric,Count')
for f in files:
    for line in get_data(f, ['Canada', 'US']):
        print(','.join(line))
