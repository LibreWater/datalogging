import psycopg2
from psycopg2 import sql
import datetime
import datetime

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
         time_stamp TIMESTAMP WITH TIME ZONE NOT NULL
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS test (
         id SERIAL PRIMARY KEY,
         description TEXT NOT NULL
    )
    """)

for command in commands:
    cursor.execute(command)

# Add some test data to the run_data table. therefore run a loop for 60 times, representing 60 minutes of data.
# The newest data is added at the end of the table and has the current system time as timestamp.
# Older data hast always the timestamp according to the loop, so the first data has the timestamp of 60 minutes ago.

an_hour_ago = datetime.datetime.now() - datetime.timedelta(minutes=60)
print(an_hour_ago)
for i in range(60):
    timestamp = an_hour_ago + datetime.timedelta(minutes=i)
    timestamp = timestamp.replace(tzinfo=datetime.timezone(datetime.timedelta(hours=1)))  # Set timezone to CET
    cursor.execute("INSERT INTO run_data (temperature, humidity, water_level, time_stamp) VALUES (%s, %s, %s, %s)", (25.0+i, 50.0+i, 0.6-i/100, timestamp))
    

cursor.close()
conn.close()