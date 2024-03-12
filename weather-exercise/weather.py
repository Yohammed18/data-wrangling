import pandas

# reading and analyzing via pandas
data = pandas.read_csv('weather_data.csv')

# print the csv file in the console
print(data)
print('\n')
# print the Condition column
print(data['condition'])
print('\n')
print(type(data))
print(type(data['condition']))
# 2 Primary data Structures of pandas are Series (1-dimensional) and DataFrame (2-dimensional). They handle the vast majority of typical use cases in most of the industries i.e. finance, statistics, social science, etc..


# turn table into dictionary
table_dictionary = data.to_dict()
print('\n')
print(f'Table into Dictionary: \n{table_dictionary}')
# turn the series into a list
temp_list = data['temp'].to_list()
print(f'Colum Temperature into a List: \n{temp_list}')

# calculate the average temperatture will be sum of the elements in the list divided by the number of elements in the list

avg_temp = round((sum(temp_list)/len(temp_list)), 2)
print(f"\nThe everage Temperature is: {avg_temp}")

mean = round(data['temp'].mean(), 2)
print(mean)
print('\n')
# get the maximum value 
maximum = data['temp'].max()
print(f'Maximum value: {maximum}')
print('\n')
# get the entiere row
mon_day = data[data['day'] == 'Monday']
print(mon_day)
print('\n')
# get the row data where the tempterature is at the maximum
maximum_row = data[data.temp == maximum]
print(maximum_row)
print('\n')
print(maximum_row.condition)
print('\n')
# convert Monday's temperature to Fahrenheit
celcius = mon_day.temp[0]
fahrenheit = (celcius*9/5) + 32
print(f'Fahrenheit: {fahrenheit}. Celcius: {celcius}')