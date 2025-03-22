import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import json

# Load JSON dataset
data_path = "/mnt/data/imdb_movies_2000to2022.prolific (1).json"
with open(data_path, "r", encoding="utf-8") as file:
    data = [json.loads(line) for line in file]

df = pd.DataFrame(data)

# Selecting relevant columns (assuming 'budget', 'rating', 'title', 'revenue', and 'genre' exist)
df = df[['title', 'budget', 'revenue', 'rating', 'genres']]

# Data Cleaning
# Remove rows with missing budget or rating values
df = df.dropna(subset=['budget', 'rating'])

# Convert budget and revenue to numeric
df['budget'] = pd.to_numeric(df['budget'], errors='coerce')
df['revenue'] = pd.to_numeric(df['revenue'], errors='coerce')

# Remove extreme outliers (e.g., budgets over $500M or unrealistic $0 budgets)
df = df[(df['budget'] > 1e6) & (df['budget'] < 5e8)]

# Exploratory Data Analysis
plt.figure(figsize=(10, 6))
sns.histplot(df['budget'], bins=30, kde=True)
plt.title("Distribution of Movie Budgets")
plt.xlabel("Budget (USD)")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(df['rating'], bins=20, kde=True)
plt.title("Distribution of IMDb Ratings")
plt.xlabel("IMDb Rating")
plt.ylabel("Frequency")
plt.show()

# Correlation Analysis
plt.figure(figsize=(8, 5))
sns.heatmap(df[['budget', 'rating', 'revenue']].corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Heatmap")
plt.show()

# Top 10 highest-budget movies
print("Top 10 Highest Budget Movies:")
print(df[['title', 'budget', 'rating']].sort_values(by='budget', ascending=False).head(10))

# Top 10 highest-rated movies
print("Top 10 Highest Rated Movies:")
print(df[['title', 'budget', 'rating']].sort_values(by='rating', ascending=False).head(10))
