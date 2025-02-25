import pandas as pd     #We import pandas for working with DataFrames and os for interacting with the file system.
#import glob
#import os

data = pd.read_csv('C:\Coffe_Shop_Project\coffee.csv')     #I am reading each diffrent .csv file individualy by using pandas and .read(). Reading data from coffee.csv file.
clean_data = pd.read_csv('C:\Coffe_Shop_Project\coffee_clean.csv')  #Reading data from coffee_clean.csv file.
id_data = pd.read_csv('C:\Coffe_Shop_Project\coffee_id.csv')  #Reading data from coffee_id.csv file.

#Data being printed from coffee.csv file.
print(data.head(10))  #This will print out the first 10 rows.
print(data.info())    #This will print the information inside the .csv file.
print(data.isnull().sum())  #This will print out missing Value.
print(data.describe()) #This will print statistical summary
print(data.nunique())  #This will check for unic values.


#Data being printed from coffee_clean.csv file.
print(clean_data.head(10))
print(clean_data.info())
print(clean_data.isnull().sum())
print(clean_data.describe())
print(clean_data.nunique())


#Data being printed from coffee_id.csv file.
print(id_data.head(10))
print(id_data.info())
print(id_data.isnull().sum())
print(id_data.describe())
print(id_data.nunique())

#Most popular products are Ethiopian Deri Kochoha, Espresso, Kenya Ruthaka Peaberry, etc. The most popular roasters are
#Flight Coffee Co., Doi Chaang Coffee, Temple Coffee and Tea, etc. The region that has the best sales performance is Africa Arabia. The sesonal
#trends will produce more reviews and rating may go up or down depending on the reviews.

