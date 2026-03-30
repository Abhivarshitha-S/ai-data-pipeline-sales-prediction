import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def predict_sales():
    # 1️⃣ Create clean synthetic data
    # quantity from 1 to 10, total_price = quantity * 1000
    data = {
        'quantity': list(range(1, 11)),
        'total_price': [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    }
    df = pd.DataFrame(data)

    print("Synthetic clean data:")
    print(df, "\n")

    # 2 Define features and target
    X = df[['quantity']]  # must be DataFrame
    y = df['total_price']

    # 3 Split data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 4 Train Linear Regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # 5 Predict on test set and evaluate
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error: {mse:.2f}\n")

    # 6 Predict for new quantity (example: 5 units)
    new_quantity = pd.DataFrame({'quantity':[5]})
    predicted_price = model.predict(new_quantity)
    print(f"Predicted total price for quantity 5: {predicted_price[0]:.2f}")

# 7 Run when executed directly
if __name__ == "__main__":
    predict_sales()