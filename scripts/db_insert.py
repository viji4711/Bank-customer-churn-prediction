import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import pandas as pd
from utils.db_connection import create_connection

# ----------- EDIT THESE --------------
CSV_PATH = "data/raw/bank_churn.csv"
TABLE_NAME = "customers"
# -------------------------------------

def load_csv(file_path):
    """Load CSV file into pandas DataFrame"""
    df = pd.read_csv(file_path)
    print("CSV Loaded Successfully!")
    print(df.head())
    return df


def clean_columns(df: pd.DataFrame):
    """Clean column names to match MySQL table names"""
    df.columns = [col.strip().replace(" ", "_") for col in df.columns]
    return df


def insert_data(df):
    conn = create_connection()
    cursor = conn.cursor()

    # Build INSERT Query Dynamically
    columns = ",".join(df.columns)
    placeholders = ",".join(["%s"] * len(df.columns))
    query = f"INSERT INTO {TABLE_NAME} ({columns}) VALUES ({placeholders})"

    # Convert DataFrame rows into list of tuples
    values = [tuple(row) for row in df.to_numpy()]

    try:
        cursor.executemany(query, values)
        conn.commit()
        print(f"Inserted {cursor.rowcount} rows successfully!")
    except Exception as e:
        print("Error inserting data:", e)
        conn.rollback()

    cursor.close()
    conn.close()


if __name__ == "__main__":
    df = load_csv(CSV_PATH)
    df = clean_columns(df)
    insert_data(df)
