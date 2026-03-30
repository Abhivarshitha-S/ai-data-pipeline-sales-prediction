import sqlite3
import pandas as pd

def query_sales():
    # Connect to database
    conn = sqlite3.connect("data/database.db")
    
    # Load data
    df = pd.read_sql_query("SELECT * FROM sales", conn)
    
    print("Sales data loaded from database:\n")
    print(df.head(), "\n")
    
    # Total sales by product
    print("Total sales by product:")
    print(df.groupby('product')['total_price'].sum(), "\n")
    
    # Top 3 products by quantity
    print("Top 3 selling products by quantity:")
    print(df.groupby('product')['quantity'].sum().sort_values(ascending=False).head(3), "\n")
    
    # Sample data view
    print("Sample quantity & price data:")
    print(df[['quantity','total_price']].head())
    
    # Close connection
    conn.close()

# Run directly
if __name__ == "__main__":
    query_sales()