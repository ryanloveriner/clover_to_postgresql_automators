# -*- coding: utf-8 -*-
"""
@author: ryanc
"""

import os
import psycopg2
from glob import glob

# --- USER CONFIGURATION ---
csv_folder = r"C:\Users\ryanc\OneDrive\Documents\Work Stuff\2024 Cafe Coffee Trends\Cleaned Clover Reports\Lupe"  # Change this
db_params = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "77-Tylerd7",
    "host": "localhost",
    "port": 5432
}

# --- DEFINE TABLE SCHEMA ---
columns = [
    ("location", "TEXT"),
    ("month", "TEXT"),
    ("name", "TEXT"),
    ("gross_sales", "NUMERIC(12,2)"),
    ("net_sales", "NUMERIC(12,2)"),
    ("sold", "INTEGER"),
    ("refunded", "INTEGER"),
    ("discounts", "NUMERIC(12,2)"),
    ("refunds", "INTEGER"),
    ("percent_net_sales", "INTEGER"),
    ("avg_item_size", "NUMERIC(6,2)"),
    ("cogs", "NUMERIC(12,2)"),
    ("gross_profit", "NUMERIC(12,2)")
]

column_names = [col[0] for col in columns]
column_defs = ",\n    ".join([f"{name} {dtype}" for name, dtype in columns])

# --- CONNECT TO POSTGRES ---
conn = psycopg2.connect(**db_params)
cur = conn.cursor()

# --- IMPORT EACH CSV ---
for file_path in glob(os.path.join(csv_folder, "*.csv")):
    table_name = os.path.splitext(os.path.basename(file_path))[0].lower().replace(" ", "_")

    print(f"Creating and importing: {table_name}")

    # Drop table if it already exists (optional)
    cur.execute(f"DROP TABLE IF EXISTS {table_name};")

    # Create table
    cur.execute(f"""
        CREATE TABLE {table_name} (
            {column_defs}
        );
    """)

    # Import CSV into table
    with open(file_path, "r", encoding="utf-8") as f:
        cur.copy_expert(f"""
            COPY {table_name}({', '.join(column_names)})
            FROM STDIN WITH CSV HEADER
        """, f)

    conn.commit()

cur.close()
conn.close()
print("✅ All CSVs imported successfully.")