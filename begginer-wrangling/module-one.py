# import panda with alias pd
import pandas as pd 
import numpy as np 

# store the csv file in a variable. (in this case we are retriving the csv file from a website)
url = 'https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-01-14/passwords.csv'

data = pd.read_csv(url)

# display the first ten records. If no paramater have been passed, the head() and tail() will the display the top/bottom 5 rows/records od the dataframe
print("TOP 5")
print(data.head())
print('\n')
print("BOTTOM 5")
print(data.tail())
print('\n')

# display the first ten records
print(data.head(10))
print('\n')
# display the last ten records
print(data.tail(10))
print('\n')


# if you want to know how many rows and columns your dataframe has use the shape function
row, column = data.shape
print(f'The DataFrame has {row} rows and {column} columns.')

# to print a synopsis on the table use the info() function while the describe() provides more of a statistical analysis of the frame
print(f"\n {data.info()}\n")
print(data.describe())

print('\n')
# to rename a column you need to reasign the dataframe or se the argument inplace=True
data.rename(columns={'password': 'secret password'}, inplace=True)

print(data['secret password'].head())
print('\n')

# print range of index
print(data.index)

# ADD/REMOVE COLUMNS
# You can add columns using the [] bracket, and drop them by simply calling drop() function.
# add Column US Citizen and set true
data['US Citizen'] = True

print(data.head())
print('\n')
# the info() is very useful. With it you'll be able to visualize the added column, the number of rows who have True assigned, as well as the data type.
print(data.info())
# drop column
print('\n')
data.drop(columns=['US Citizen'], inplace=True)
data.info()
print('\n')
# ADD/REMOVE ROWS
# we can add by using loc() and drop() to drop rows. The append() function has been deprecated and it's no longer available 
data.loc[len(data.index)] = ['1234!@#$qwerQWER', 'unrelated password',  6.7,  'minutes', 0.000040, 4, 4, 5, 6]
print(data.tail())
print('\n')
# drop the rows from 500 down
data.drop(index=range(500, len(data.index)), inplace=True)
print(data.tail())

# To learn more about the basic on data wranglign visit the page https://www.tomasbeuzen.com/python-programming-for-data-science/chapters/chapter8-wrangling-basics.html. 
