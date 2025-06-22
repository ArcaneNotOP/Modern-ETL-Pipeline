import pandas as pd
import psycopg2

# Load data from CSV
df = pd.read_csv('./data/dailyActivity_merged.csv')
print(f"✅ Loaded {len(df)} rows")

# Transform: Clean data
df.dropna(inplace=True)
print(f"✅ Cleaned: {len(df)} rows after dropping empty")

# Load: Insert data into PostgreSQL
try:
    # Connect to the database (Postgres container from Docker)
    conn = psycopg2.connect(
        dbname="etldb",
        user="admin",
        password="admin",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()

    # Create table if not exists
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id Serial PRIMARY KEY,
        ActivityDate DATE,
        TotalSteps INTEGER,
        TrackerDistance DOUBLE PRECISION         
    );
    """)

    # Insert each row
    for _, row in df.iterrows():
        cur.execute(
            "INSERT INTO users (ActivityDate,TotalSteps,TrackerDistance) VALUES (%s,%s,%s)",
            (row['ActivityDate'],row['TotalSteps'],row['TrackerDistance'])
        )

    conn.commit()
    print("✅ Data inserted successfully!")

except Exception as e:
    print("❌ ETL failed:", e)

finally:
    if conn:
        cur.close()
        conn.close()