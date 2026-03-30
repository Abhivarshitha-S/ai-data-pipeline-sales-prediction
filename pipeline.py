# pipeline.py
from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data
from sql.query import query_sales
from ai.predict import predict_sales

def main():
    print("\n------- ETL PROCESS -------\n")
    # 1 ETL
    data = extract_data()          # extract data from source
    transformed_data = transform_data(data)  # transform
    load_data(transformed_data)    # load into database
    print("\nETL completed successfully!\n")

    print("\n------- SQL QUERIES ---------\n")
    # 2 SQL
    query_sales()  # run your queries / aggregations
    print("\nSQL queries completed successfully!\n")

    print("\n------- AI PREDICTION -------\n")
    # 3 AI
    predict_sales()  # clean data, train model, predict
    print("\nAI prediction completed successfully!\n")

# Run pipeline when executed directly
if __name__ == "__main__":
    main()