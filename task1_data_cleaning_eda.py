import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# -----------------------------
# FILE PATHS
# -----------------------------

# Get the folder where this Python file is located
project_folder = Path(__file__).parent
plots_folder = project_folder / "plots"

# Create the plots folder if it does not already exist
plots_folder.mkdir(exist_ok=True)


# -----------------------------
# LOAD DATASET
# -----------------------------

df = sns.load_dataset("titanic")

print("Dataset loaded successfully!")
print(df.head())


# -----------------------------
# DATA INSPECTION
# -----------------------------

print("\nDataset shape:")
print(df.shape)

print("\nColumn names:")
print(df.columns)

print("\nDataset information:")
df.info()

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())


# -----------------------------
# DATA CLEANING
# -----------------------------

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing age values with the median
df["age"] = df["age"].fillna(df["age"].median())

# Fill missing embarked values with the most common value
df["embarked"] = df["embarked"].fillna(df["embarked"].mode()[0])

# Drop columns with too many missing values or redundant information
df = df.drop(columns=["deck", "embark_town"])

# Remove duplicates that may have appeared after cleaning
df = df.drop_duplicates()

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nDuplicate rows after cleaning:")
print(df.duplicated().sum())

print("\nCleaned dataset shape:")
print(df.shape)


# -----------------------------
# OUTLIER DETECTION
# -----------------------------

# Calculate the IQR for the fare column
Q1 = df["fare"].quantile(0.25)
Q3 = df["fare"].quantile(0.75)
IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

# Identify potential outliers
outliers = df[
    (df["fare"] < lower_limit) |
    (df["fare"] > upper_limit)
]

print("\nOutlier analysis for fare:")
print("Lower limit:", lower_limit)
print("Upper limit:", upper_limit)
print("Number of potential outliers:", len(outliers))

# Potential fare outliers are retained because they may represent
# genuine high fares rather than incorrect data.


# -----------------------------
# EXPLORATORY DATA ANALYSIS
# -----------------------------

print("\nStatistical summary:")
print(df.describe())


# -----------------------------
# VISUALIZATION 1: HISTOGRAM
# -----------------------------

plt.figure(figsize=(8, 5))
plt.hist(df["age"], bins=20, edgecolor="black")
plt.title("Distribution of Passenger Ages")
plt.xlabel("Age")
plt.ylabel("Number of Passengers")
plt.savefig(plots_folder / "age_distribution.png")
plt.close()


# -----------------------------
# VISUALIZATION 2: BAR CHART
# -----------------------------

class_counts = df["class"].value_counts().sort_index()

plt.figure(figsize=(8, 5))
plt.bar(class_counts.index.astype(str), class_counts.values)
plt.title("Number of Passengers by Class")
plt.xlabel("Passenger Class")
plt.ylabel("Number of Passengers")
plt.savefig(plots_folder / "passengers_by_class.png")
plt.close()


# -----------------------------
# VISUALIZATION 3: BOX PLOT
# -----------------------------

plt.figure(figsize=(8, 5))
plt.boxplot(df["fare"])
plt.title("Distribution of Passenger Fares")
plt.ylabel("Fare")
plt.savefig(plots_folder / "fare_boxplot.png")
plt.close()


# -----------------------------
# VISUALIZATION 4: CORRELATION HEATMAP
# -----------------------------

numeric_df = df.select_dtypes(include=np.number)

plt.figure(figsize=(10, 7))
sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("Correlation Heatmap")
plt.savefig(plots_folder / "correlation_heatmap.png")
plt.close()


# -----------------------------
# SURVIVAL ANALYSIS
# -----------------------------

# Survival rate by gender
gender_survival = df.groupby(
    "sex", observed=True
)["survived"].mean() * 100

print("\nSurvival rate by gender:")
print(gender_survival)


# Survival rate by passenger class
class_survival = df.groupby(
    "class", observed=True
)["survived"].mean() * 100

print("\nSurvival rate by passenger class:")
print(class_survival)


# -----------------------------
# VISUALIZATION 5: SURVIVAL RATE
# -----------------------------

plt.figure(figsize=(8, 5))
plt.bar(
    class_survival.index.astype(str),
    class_survival.values
)
plt.title("Survival Rate by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate (%)")
plt.savefig(plots_folder / "survival_rate_by_class.png")
plt.close()

# Save the cleaned dataset
cleaned_data_path = project_folder / "cleaned_titanic_dataset.csv"
df.to_csv(cleaned_data_path, index=False)

print("\nCleaned dataset saved successfully!")

print("\nAnalysis completed successfully!")