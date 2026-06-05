import numpy as np
import pandas as pd
#creating a series
#a pandas seies is like a column in a table
#a series is a 1-D array for holding data of any type
s = pd.Series([1,2,3,4,5])
print(s)
print(s[4])
#creating a label with index arguments
a = pd.Series([6,7,8,9,10], index=['a', 'b', 'c', 'd', 'e'])
print(a['b'])
#creating a series like a dictionary
data = { 'name' : ["maria", "meimei", "maki"],
  'age' : [19, 19, 19],
  }
b = pd.Series(data)
print(b)
#here the keys of the dictionary becomes labels
print(b['name'])

#dataframes are multidimensional tables in pandas
#creating a dataframe with two series
c = pd.DataFrame(data)
print(c)
#loading a csv file into a DataFrame
df = pd.read_csv("C:\\Users\\kau13192\\Downloads\\data.csv")
print(df)
#to print the entire DataSet, use to_string() function
#JSON is a plain text, but has the format of an object. 
#big datasets are often stored, or extracted as JSON files
#JSON objects have the same format as a Python dictionary, so we can easily convert JSON to a DataFrame
#loading a python dictionary into a DataFrame
data2 = {
    "name": ["maria", "meimei", "maki"],
    "age": [19, 18, 17],
    "city": ["new york", "los angeles", "chicago"]
}
df2 = pd.DataFrame(data2)
print(df2)
print("\n Analysing DataFrames \n")
#to get an overview of the DataFrame:
print(df.head())
# to view the last rows of a DataFrame, use the tail() function
print(df.tail())
#To get info about the DataFrame
print(df.info())
print("\n Data Cleaning  \n")
#removing empty rows
df3 = df.dropna()
print(df3)
# df.dropna(inplace=True)
# print(df)
#replacing empty cells
df4 = df.fillna(777)
print(df4)
df5 = df.fillna({"Calories": 44444})
print(df5)
x = df["Calories"].mean()
print("Mean = " + str(x))
print("Median = " + str(df["Calories"].median()))
print("Mode = " + str(df["Calories"].mode()))
#replacing values
df.loc[7,'Duration'] = 111
print(df)
