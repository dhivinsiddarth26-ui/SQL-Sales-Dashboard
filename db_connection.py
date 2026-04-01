import psycopg2
import pandas as pd

def get_data():
    conn = psycopg2.connect(
        host="localhost",
        database="datascience_db",
        user="postgres",
        password="dhivin08"
    )

    query = "SELECT * FROM sales;"
    df = pd.read_sql(query, conn)

    conn.close()
    return df