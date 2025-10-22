import pandas as pd
from sqlalchemy import create_engine
import os

# --- IMPORTANT: SET UP YOUR DATABASE CONNECTION ---
# 1. In your Supabase project, go to Project Settings > Database.
# 2. Find your Connection String (it looks like: "postgresql://postgres:[YOUR-PASSWORD]@[...].supabase.co:5432/postgres").
# 3. Replace the placeholder below with your actual connection string.
#    IMPORTANT: Replace [YOUR-PASSWORD] with your actual database password.
DB_CONNECTION_STRING = "postgresql://postgres:8919492311V!!@db.bhqnoqxosrxolovxcrnk.supabase.co:5432/postgres"

# The name of the CSV file you saved
CSV_FILENAME = "data_set.csv"

# The name you want for the table in your database
TABLE_NAME = "groundwater_data"

def upload_csv_to_db():
    """
    Connects to the PostgreSQL database, reads the master CSV file,
    and uploads its entire contents to a new table.
    """
    print("--- Starting Data Upload Process ---")

    if not os.path.exists(CSV_FILENAME):
        print(f"FATAL ERROR: The file '{CSV_FILENAME}' was not found.")
        print("Please make sure it's in the same folder as this script.")
        return

    if "YourPassword" in DB_CONNECTION_STRING:
        print("FATAL ERROR: Please update the 'DB_CONNECTION_STRING' with your real Supabase password and details.")
        return

    try:
        print(f"Reading '{CSV_FILENAME}' into memory...")
        df = pd.read_csv(CSV_FILENAME)
        
        # Clean up column names to be SQL-friendly (lowercase, no special chars)
        df.columns = [col.lower().replace(' ', '_').replace('(', '').replace(')', '') for col in df.columns]
        
        print(f"Connecting to the database...")
        # Create a database engine
        engine = create_engine(DB_CONNECTION_STRING)

        print(f"Uploading {len(df)} rows to the table '{TABLE_NAME}'...")
        # This will create the table and insert all the data.
        # 'if_exists='replace'' will drop the table if it already exists and create a new one.
        # Use 'if_exists='append'' if you want to add data to an existing table.
        df.to_sql(TABLE_NAME, engine, if_exists='replace', index=False)

        print("\n--- SUCCESS! ---")
        print(f"The data has been uploaded to your PostgreSQL database in the '{TABLE_NAME}' table.")

    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    upload_csv_to_db()
