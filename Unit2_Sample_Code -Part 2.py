# Unit 2 Sample Code – Reading, Writing, and Inspecting CSV Data
# Version 2 – with extra practice tasks

import pandas as pd

# -----------------------------------------
# PART 0 – EXAMPLE: CODE WE WALKED THROUGH
# -----------------------------------------

# Read the CSV file into a DataFrame
df = pd.read_csv("IndieQuest_GameSales.csv")

print("First 5 rows (example):")
print(df.head())
print()

print("Last 3 rows (example):")
print(df.tail(3))
print()

print("DataFrame info (example):")
print(df.info())
print()

print("Numeric summary (describe) – example:")
print(df.describe())
print()

# Create a sample of the first 10 rows (example)
df_sample = df.head(10)

print("Sample of first 10 rows (example):")
print(df_sample)
print()

# Save the sample to CSV without index (example)
df_sample.to_csv("IndieQuest_sample10.csv", index=False)
print("Saved IndieQuest_sample10.csv")
print("-" * 60)

# ----------------------------------------------------
# PART 1 – YOUR TURN: PRACTICE TASKS FOR UNIT 2
# (These should align with your worksheet work)
# ----------------------------------------------------

# TASK 1: Show a different “head” sample
# TODO: Show the first 8 rows instead of 5.
print("TASK 1 – First 8 rows:")
print(df.head(8))
print()

# TASK 2: Look at a different “tail” sample
# TODO: Show the last 7 rows of the DataFrame.
print("TASK 2 – Last 7 rows:")
print(df.tail(7))
print()

# TASK 3: Practice using info() to focus on one column
# TODO: Print just the data type of the Revenue column.
print("TASK 3 – Revenue column dtype:")
print(df["Revenue"].dtype)
print()

# TASK 4: Use describe() **only for Rating**
# TODO: Compute and print descriptive stats for the Rating column alone.
print("TASK 4 – Rating describe():")
print(df["Rating"].describe())
print()

# TASK 5: Count missing values in a numeric column
# TODO: Print how many missing values there are in Revenue.
print("TASK 5 – Missing values in Revenue:")
print(df["Revenue"].isna().sum())
print()

# TASK 6: Make a NEW sample and save it
# TODO: Create a DataFrame called df_last10 with the last 10 rows.
df_last10 = df.tail(10)

print("TASK 6 – Sample of last 10 rows:")
print(df_last10)
print()

# TODO: Save df_last10 to a CSV called "IndieQuest_sample_last10.csv" without the index.
df_last10.to_csv("IndieQuest_sample_last10.csv", index=False)
print("Saved IndieQuest_sample_last10.csv")
print("-" * 60)

# TASK 7: Challenge – high revenue games only
# TODO: Create df_high_revenue with only games where Revenue > 1_000_000
df_high_revenue = df[df["Revenue"] > 1_000_000]

print("TASK 7 – High revenue games (Revenue > 1,000,000):")
print(df_high_revenue.head())
print()

# TODO: Save df_high_revenue to "IndieQuest_highRevenue.csv" without index.
t1 = df.head(10)
df_high_revenue.to_csv("IndieQuest_highRevenue.csv", index=False)

t1.to_csv("IndieQuest_highRevenue.csv")


print("Saved IndieQuest_highRevenue.csv")
