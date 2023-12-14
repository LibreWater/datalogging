import psycopg2
from psycopg2 import sql

# Define your database credentials
params = {
    "dbname": "acraea_db",
    "user": "acraea",
    "password": "turtle_power",
    "host": "localhost",
    "port": 5433
}

# Connect to the PostgreSQL server
conn = psycopg2.connect(**params)

# Create a new database
conn.autocommit = True  # Set autocommit to True
cursor = conn.cursor()

# Create tables
commands = (
    """
    CREATE TABLE IF NOT EXISTS run_data (
         id SERIAL PRIMARY KEY,
         temperature FLOAT NOT NULL,
         humidity FLOAT NOT NULL,
         water_level FLOAT NOT NULL,
         time_stamp TIMESTAMP NOT NULL
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS test (
         id SERIAL PRIMARY KEY,
         description TEXT NOT NULL
    )
    """
)
for command in commands:
    cursor.execute(command)

# Add some test data to the run_data table
cursor.execute("INSERT INTO run_data (temperature, humidity, water_level, time_stamp) VALUES (%s, %s, %s, %s)", (25.0, 50.0, 0.6, '2020-01-01 00:00:00'))
cursor.execute("INSERT INTO run_data (temperature, humidity, water_level, time_stamp) VALUES (%s, %s, %s, %s)", (26.0, 51.0, 0.5, '2020-01-01 00:00:01'))
cursor.execute("INSERT INTO run_data (temperature, humidity, water_level, time_stamp) VALUES (%s, %s, %s, %s)", (27.0, 52.0, 0.4, '2020-01-01 00:00:02'))
cursor.execute("INSERT INTO run_data (temperature, humidity, water_level, time_stamp) VALUES (%s, %s, %s, %s)", (28.0, 53.0, 0.3, '2020-01-01 00:00:03'))

cursor.close()
conn.close()