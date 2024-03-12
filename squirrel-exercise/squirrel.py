import pandas

# import the squirrel census csv file from 2018
data = pandas.read_csv('2018 Central Park Squirrel Census - Squirrel Data.csv')

# store all the value under column 'Primary Fur Color' for Gray, Black, Cinnamon
gray_count = len(data[data['Primary Fur Color'] == 'Gray'])
black_count = len(data[data['Primary Fur Color'] == 'Black'])
cinnamon_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])

# store values into dictionary
dict_fur = {
    'Fur Color': ['Gray', 'Black', 'Cinnamon'],
    'Count': [gray_count, black_count, cinnamon_count]
}

# turn dict into Dataframe
fur_frame = pandas.DataFrame(dict_fur)
print(fur_frame)
fur_frame.to_csv('squirrel_count.csv')



# SEPERATE EXERCISE
# Create a sample DataFrame
data = {'City': ['City1', 'City2', 'City3'],
        'Temperature_Celsius': [25, 18, 30]}

df = pandas.DataFrame(data)

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Apply the conversion function to the 'Temperature_Celsius' column
df['Temperature_Fahrenheit'] = df['Temperature_Celsius'].apply(celsius_to_fahrenheit)

# Display the DataFrame
print(df)
