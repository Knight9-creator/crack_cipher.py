# Unit 2 Sample Code – Reading, Writing, and Inspecting CSV Data

import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv("IndieQuest_GameSales.csv")

print("First 5 rows:")
print(df.head())
print()

print("Last 3 rows:")
print(df.tail(3))
print()

print("DataFrame info:")
print(df.info())
print()

print("Numeric summary (describe):")
print(df.describe())
print()

# Create a sample of the first 10 rows
df_sample = df.head(10)

print("Sample of first 10 rows:")
print(df_sample)
print()

# Save the sample to CSV without index
df_sample.to_csv("IndieQuest_sample10.csv", index=False)
print("Saved IndieQuest_sample10.csv")
