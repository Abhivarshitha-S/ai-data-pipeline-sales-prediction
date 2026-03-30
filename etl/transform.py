def transform_data(df):
    print("Cleaning data...")

    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values
    df = df.fillna(0)

    # Convert column names to lowercase
    df.columns = df.columns.str.lower()

    # Create new column
    if 'quantity' in df.columns and 'price' in df.columns:
        df['total_price'] = df['quantity'] * df['price']

    print("Data cleaned")
    return df