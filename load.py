import psycopg2
from extract import df
from transform import transform

df = transform(df)

conn = psycopg2.connect(
    dbname="airline_db",
    user="postgres",
    password="your_password",
    host="localhost"
)

cursor = conn.cursor()

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO flight_fact (airline, origin, destination, departure_delay, arrival_delay, distance, flight_date)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, tuple(row))

conn.commit()
cursor.close()
conn.close()

print("Data Loaded Successfully!")