import psycopg2
from psycopg2 import sql

# Define your database credentials
params = {
   "dbname": "acraea_db",
   "user": "acraea",
   "password": "turtle_power",
   "host": "localhost"
}

# Connect to the PostgreSQL server
conn = psycopg2.connect(**params)

# Create a new database
cursor = conn.cursor()
cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(params["dbname"])))

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

cursor.close()
conn.close()