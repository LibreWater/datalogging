import psycopg2
from psycopg2 import sql
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

conn.autocommit = True  # Set autocommit to True
cursor = conn.cursor()

# Create the tables if they don't exist

commands = (
    """
    CREATE TABLE IF NOT EXISTS runs (
         id SERIAL PRIMARY KEY,
         description TEXT NOT NULL,
         start_time TIMESTAMP WITH TIME ZONE NOT NULL,
         end_time TIMESTAMP WITH TIME ZONE
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS run_data (
         id SERIAL PRIMARY KEY,
         run_id INTEGER REFERENCES runs(id),
         temperature FLOAT NOT NULL,
         humidity FLOAT NOT NULL,
         water_level FLOAT NOT NULL,
         time_stamp TIMESTAMP WITH TIME ZONE NOT NULL
    )
    """
    )


for command in commands:
    cursor.execute(command)


# Add some test data to the run_data table. therefore run a loop for 60 times, representing 60 minutes of data.
# The newest data is added at the end of the table and has the current system time as timestamp.
# Older data hast always the timestamp according to the loop, so the first data has the timestamp of 60 minutes ago.

an_hour_ago = datetime.datetime.now() - datetime.timedelta(minutes=60)

start_time = an_hour_ago.replace(tzinfo=datetime.timezone(datetime.timedelta(hours=1)))  # Set timezone to CET

# insert a new run and get the id of the run
cursor.execute("INSERT INTO runs (description, start_time, end_time) VALUES (%s, %s, %s)", ("Test run", start_time, start_time))
cursor.execute("SELECT id FROM runs ORDER BY id DESC LIMIT 1")
run_id = cursor.fetchone()[0]

# insert data for the run
for i in range(60):
    timestamp = an_hour_ago + datetime.timedelta(minutes=i)
    timestamp = timestamp.replace(tzinfo=datetime.timezone(datetime.timedelta(hours=1)))  # Set timezone to CET
    cursor.execute("INSERT INTO run_data (run_id, temperature, humidity, water_level, time_stamp) VALUES (%s, %s, %s, %s, %s)", (run_id, 25.0+i, 50.0+i, 0.6-i/100, timestamp))
    # update the end_time of the run 
    cursor.execute("UPDATE runs SET end_time = %s WHERE id = %s", (timestamp, 1))


cursor.close()
conn.close()