import pandas as pd
import os

print("Reading Bronze data...")

df = pd.read_csv("data/bronze/ai4i2020_bronze.csv")

print(f"Rows before cleaning: {len(df)}")

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows with missing values
df = df.dropna()

print(f"Rows after cleaning: {len(df)}")

# Create silver folder if it doesn't exist
os.makedirs("data/silver", exist_ok=True)

# Save cleaned data
df.to_csv("data/silver/ai4i2020_silver.csv", index=False)

print("Silver layer created successfully!")