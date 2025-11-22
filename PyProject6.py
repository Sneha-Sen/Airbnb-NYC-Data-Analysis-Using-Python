#Importing All Dependencies

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#Loading Datsets
df= pd.read_csv("datasets.csv")

#Initial Exploration

#print(df.head())
#print(df.tail())
#print(df.shape)
#print(df.info())
#print(df.describe())

#Data Cleaning

#print(df.isnull().sum())
df.dropna(inplace=True)
#print(df.isnull().sum())
#print(df.duplicated().sum())
df.drop_duplicates(inplace=True)
#print(df.duplicated().sum())
#print(df.dtypes)
df['id'] = df['id'].astype(object)
df['host_id'] = df['host_id'].astype(object)
#print(df.dtypes)

# Data Analysis

# idenfying outliers in price
df1 = df[df['price'] < 1500]
#sns.boxplot(data=df1, x='price')
#plt.show()

#Price distribuion
#plt.figure(figsize=(8, 5))
#sns.histplot(data=df1, x='price', bins=100)
#plt.title('Price Distribuition')
#plt.ylabel("Frequency")
#plt.show()

#Availability distribuion
'''
plt.figure(figsize=(6, 3))
sns.histplot(data=df, x='availability_365')
plt.title('availability_365 Distribuition')
plt.ylabel("Frequency")
plt.show()
'''
#print(df1.groupby(by='neighbourhood_group')['price'].mean())
df1['price per bed']= df1['price']/df1['beds']
# average price per bed
#print(df1.groupby(by='neighbourhood_group')['price per bed'].mean())

#Bi Variable Analysis

# price dependency on neighbourhood
#sns.barplot(data=df1, x='neighbourhood_group', y='price', hue='room_type')
#plt.show()
# number of reviews and price rel
#plt.figure(figsize=(8, 5))
#plt.title("Locality and Review Dependency")
#sns.scatterplot(data=df1, x='number_of_reviews', y='price', hue='neighbourhood_group')
#plt.show()
#sns.pairplot(data=df1, vars=['price', 'minimum_nights', 'number_of_reviews', 'availability_365'], hue='room_type')
#plt.show()
#Geographical Distribution of AirBnb Listing
#plt.figure(figsize=(10, 7))
#sns.scatterplot(data=df1, x='longitude', y='latitude', hue='room_type')
#plt.title("Geographical Distribution of AirBnb Listing")
#plt.show()
# heat map - correlation of one variable with others for numerical column

corr = df1[['latitude', 'longitude', 'price', 'minimum_nights', 'number_of_reviews', 'reviews_per_month', 'availability_365', 'beds']].corr()
print(corr)
plt.figure(figsize=(8, 6))
sns.heatmap(data=corr, annot=True)
plt.show()