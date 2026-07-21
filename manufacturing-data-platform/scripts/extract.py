import pandas as pd
import os

# Read the original dataset
df = pd.read_csv("data/ai4i2020.csv")

# Create bronze folder if it doesn't exist
os.makedirs("data/bronze", exist_ok=True)

# Save raw data
df.to_csv("data/bronze/ai4i2020_bronze.csv", index=False)

print("Bronze layer created successfully!")
