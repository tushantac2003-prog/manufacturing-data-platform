import pandas as pd
import os

# -----------------------------
# Read Silver Layer
# -----------------------------

silver_path = "data/silver/ai4i2020_silver.csv"

print("Reading Silver Layer...")
df = pd.read_csv(silver_path)

# Create Gold folder if it doesn't exist
os.makedirs("data/gold", exist_ok=True)

# =====================================================
# 1. Manufacturing Summary
# =====================================================

manufacturing_summary = pd.DataFrame({
    "total_machines": [len(df)],
    "total_failures": [df["Machine failure"].sum()],
    "failure_rate (%)": [round(df["Machine failure"].mean() , 2)],
    "avg_air_temperature": [round(df["Air temperature [K]"].mean(), 2)],
    "avg_process_temperature": [round(df["Process temperature [K]"].mean(), 2)],
    "avg_rpm": [round(df["Rotational speed [rpm]"].mean(), 2)],
    "avg_torque": [round(df["Torque [Nm]"].mean(), 2)],
    "avg_tool_wear": [round(df["Tool wear [min]"].mean(), 2)]
})

manufacturing_summary.to_csv(
    "data/gold/manufacturing_summary.csv",
    index=False
)

# =====================================================
# 2. Product Type Summary
# =====================================================

product_summary = (
    df.groupby("Type")
      .agg(
          machine_count=("Type", "count"),
          failure_count=("Machine failure", "sum")
      )
      .reset_index()
)

product_summary["failure_rate (%)"] = round(
    product_summary["failure_count"] /
    product_summary["machine_count"] * 100,
    2
)

product_summary.to_csv(
    "data/gold/product_type_summary.csv",
    index=False
)

# =====================================================
# 3. Failure Type Summary
# =====================================================

failure_summary = pd.DataFrame({
    "Failure Type": [
        "Tool Wear",
        "Heat Dissipation",
        "Power Failure",
        "Overstrain",
        "Random Failure"
    ],
    "Count": [
        df["TWF"].sum(),
        df["HDF"].sum(),
        df["PWF"].sum(),
        df["OSF"].sum(),
        df["RNF"].sum()
    ]
})

failure_summary.to_csv(
    "data/gold/failure_type_summary.csv",
    index=False
)

# =====================================================
# 4. Temperature Summary
# =====================================================

temperature_summary = pd.DataFrame({
    "Metric": ["Average", "Minimum", "Maximum"],
    "Air Temperature": [
        df["Air temperature [K]"].mean(),
        df["Air temperature [K]"].min(),
        df["Air temperature [K]"].max()
    ],
    "Process Temperature": [
        df["Process temperature [K]"].mean(),
        df["Process temperature [K]"].min(),
        df["Process temperature [K]"].max()
    ]
})

temperature_summary.to_csv(
    "data/gold/temperature_summary.csv",
    index=False
)

# =====================================================
# 5. RPM Summary
# =====================================================

rpm_summary = pd.DataFrame({
    "Metric": ["Average", "Minimum", "Maximum"],
    "RPM": [
        df["Rotational speed [rpm]"].mean(),
        df["Rotational speed [rpm]"].min(),
        df["Rotational speed [rpm]"].max()
    ]
})

rpm_summary.to_csv(
    "data/gold/rpm_summary.csv",
    index=False
)

# =====================================================
# 6. Torque Summary
# =====================================================

torque_summary = pd.DataFrame({
    "Metric": ["Average", "Minimum", "Maximum"],
    "Torque": [
        df["Torque [Nm]"].mean(),
        df["Torque [Nm]"].min(),
        df["Torque [Nm]"].max()
    ]
})

torque_summary.to_csv(
    "data/gold/torque_summary.csv",
    index=False
)

# =====================================================
# 7. Tool Wear Summary
# =====================================================

toolwear_summary = pd.DataFrame({
    "Metric": ["Average", "Minimum", "Maximum"],
    "Tool Wear": [
        df["Tool wear [min]"].mean(),
        df["Tool wear [min]"].min(),
        df["Tool wear [min]"].max()
    ]
})

toolwear_summary.to_csv(
    "data/gold/tool_wear_summary.csv",
    index=False
)

# =====================================================
# 8. Machine Health (Full Dataset)
# =====================================================

machine_health = df.copy()

machine_health["Health Status"] = machine_health["Machine failure"].apply(
    lambda x: "Critical" if x == 1 else "Healthy"
)

# Save ALL original columns plus Health Status
machine_health.to_csv(
    "data/gold/machine_health.csv",
    index=False
)

print("===================================")
print("Gold Layer Created Successfully!")
print("8 Gold Tables Generated")
print("===================================")