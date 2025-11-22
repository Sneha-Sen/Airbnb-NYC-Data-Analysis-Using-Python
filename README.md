# Airbnb-NYC-Data-Analysis-Using-Python

This project provides a complete exploratory data analysis (EDA) on an Airbnb dataset using Python, covering data cleaning, preprocessing, visualization, and insight generation.

# Project Overview

The goal of this project is to analyze Airbnb listings and understand:

Price distribution

How location impacts pricing

Availability trends

Relationship between reviews and listing price

Correlation among key variables

The workflow follows a standard DA process — from loading data to generating insights.

# Technologies Used

Python

Pandas

NumPy

Matplotlib

Seaborn

# Steps Performed in Analysis
1. Data Loading

Loaded dataset using pandas.read_csv().

2. Initial Exploration

Checked .head(), .tail(), .info(), .describe()

Verified null values & duplicates.

3. Data Cleaning

Dropped missing values

Removed duplicate entries

Converted id and host_id to object datatype

Filtered out extreme outliers (price < 1500)

4. Feature Engineering

Created a new column:
price per bed = price / beds

5. Data Visualization

Used Seaborn & Matplotlib to generate:

Price distribution

Availability distribution

Price vs Neighbourhood (bar plot)

Reviews vs Price (scatter plot)

Pairplot of main numerical features

Geographic distribution (Latitude / Longitude)

Heatmap of variable correlations

6. Correlation Heatmap

Visualized relationships between:

price

minimum_nights

number_of_reviews

reviews_per_month

availability_365

latitude / longitude

beds

# Key Insights

- Listings in certain neighbourhood groups are significantly costlier.
- Price is moderately affected by location and type of room.
- Number of reviews doesn’t strongly control price — people pay more for location & room type.
- Beds count influences price, making price-per-bed a useful metric.
- Strong correlations are mostly geographic (latitude-longitude).

# Conclusion

It demonstrates skills in:
Data cleaning
Exploratory analysis
Visualization
Business insight generation
