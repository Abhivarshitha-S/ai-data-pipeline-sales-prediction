import sqlite3

def load_data(df):
    conn = sqlite3.connect("data/database.db")

    df.to_sql("sales", conn, if_exists="replace", index=False)

    conn.close()
    print("Data loaded into database")