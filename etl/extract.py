import pandas as pd

def extract_data():
    file_path = "data/raw_data.csv"
    df = pd.read_csv(file_path)
    
    print("Data Loaded Successfully")
    return df