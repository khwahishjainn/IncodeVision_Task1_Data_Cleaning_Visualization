# Titanic Dataset - Data Cleaning and Exploratory Data Analysis

## Overview

This project was completed as part of my Data Science internship at IncodeVision.

The project focuses on data cleaning, exploratory data analysis (EDA), and visualization using the Titanic dataset.

## Objectives

- Clean and preprocess the dataset
- Handle missing values
- Remove duplicate records
- Inspect dataset structure and data types
- Identify potential outliers
- Explore patterns and relationships in the data
- Create visualizations to communicate findings

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

## Dataset

The Titanic dataset contains information about passengers aboard the Titanic, including:

- Passenger class
- Sex
- Age
- Fare
- Number of siblings/spouses
- Number of parents/children
- Survival status

## Data Cleaning

The following preprocessing steps were performed:

1. Removed duplicate rows.
2. Filled missing age values using the median age.
3. Filled missing embarkation values using the most frequent value.
4. Removed the `deck` column because it contained a large number of missing values.
5. Removed the redundant `embark_town` column.
6. Checked for remaining missing values and duplicates.

## Outlier Analysis

The Interquartile Range (IQR) method was used to identify potential outliers in passenger fares.

Potential high-fare values were identified and retained because they may represent genuine passenger fares rather than incorrect data.

## Exploratory Data Analysis

The following visualizations were created:

- Passenger age distribution histogram
- Number of passengers by class bar chart
- Passenger fare box plot
- Numerical correlation heatmap
- Survival rate by passenger class

## Key Findings

- Most passengers were concentrated around the 20–30 age range.
- Third-class passengers formed the largest passenger group.
- Several high passenger fares were identified as potential outliers.
- Female passengers had a substantially higher survival rate than male passengers.
- Survival rate was highest among first-class passengers and lowest among third-class passengers.
- Passenger class showed a moderate negative correlation with survival, while fare showed a weak positive correlation.

## Project Structure

```text
Task_1_Data_Cleaning_Visualization/
│
├── plots/
│   ├── age_distribution.png
│   ├── passengers_by_class.png
│   ├── fare_boxplot.png
│   ├── correlation_heatmap.png
│   └── survival_rate_by_class.png
│
├── cleaned_titanic_dataset.csv
├── task1_data_cleaning_eda.py
└── README.md
```

## Conclusion

This project provided practical experience in data preprocessing, exploratory data analysis, outlier detection, and data visualization using Python.
