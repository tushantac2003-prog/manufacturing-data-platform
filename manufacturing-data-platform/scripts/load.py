import os
import pandas as pd
from sqlalchemy import create_engine, text

# =====================================================
# PostgreSQL Connection
# =====================================================
engine = create_engine(
    "postgresql+psycopg2://airflow:airflow@postgres:5432/airflow",
    echo=False
)

# =====================================================
# Check Database Connection
# =====================================================
print("=" * 60)
print("Connecting to PostgreSQL...")
print("=" * 60)

with engine.connect() as conn:
    result = conn.execute(
        text("SELECT current_database(), current_schema(), current_user")
    )
    db_name, schema_name, user_name = result.fetchone()

    print(f"Database : {db_name}")
    print(f"Schema   : {schema_name}")
    print(f"User     : {user_name}")

print("=" * 60)

# =====================================================
# Gold Layer Path
# =====================================================
gold_path = "/opt/airflow/data/gold"

tables = {
    "manufacturing_summary.csv": "manufacturing_summary",
    "product_type_summary.csv": "product_type_summary",
    "failure_type_summary.csv": "failure_type_summary",
    "temperature_summary.csv": "temperature_summary",
    "rpm_summary.csv": "rpm_summary",
    "torque_summary.csv": "torque_summary",
    "tool_wear_summary.csv": "tool_wear_summary",
    "machine_health.csv": "machine_health"
}

print("Loading Gold Layer into PostgreSQL...")
print("=" * 60)

for file_name, table_name in tables.items():

    file_path = os.path.join(gold_path, file_name)

    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_name}")
        continue

    print(f"\nLoading {file_name}")

    df = pd.read_csv(file_path)

    print(f"Rows    : {len(df)}")
    print(f"Columns : {len(df.columns)}")

    df.to_sql(
        table_name,
        engine,
        schema="public",
        if_exists="replace",
        index=False
    )

    print(f"✅ {table_name} loaded successfully.")

print("\n" + "=" * 60)
print("Verifying tables in PostgreSQL...")
print("=" * 60)

with engine.connect() as conn:

    result = conn.execute(text("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema='public'
        ORDER BY table_name;
    """))

    tables_found = result.fetchall()

    print("\nTables Present:\n")

    for table in tables_found:
        print(table[0])

print("\n" + "=" * 60)
print("Gold Layer Loaded Successfully!")
print("=" * 60)