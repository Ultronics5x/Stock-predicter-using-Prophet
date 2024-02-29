Stock-prediction-using-Time-series-and-Streamlit-for-frontend
This Python script utilizes Streamlit to create a stock prediction app. Here's a summary of its functionality:

1. **Data Loading and Selection**:
   - Users can input a stock ticker or choose from examples (AAPL, GOOG, MSFT, GME).
   - They can select the dataset for prediction and specify the number of years for forecasting.

2. **Data Visualization**:
   - The app displays raw stock data, including open and close prices, in a time series format.

3. **Forecasting**:
   - The script uses the Prophet library for time series forecasting.
   - It trains the model on the selected stock's closing prices and forecasts future prices.
   - Evaluation metrics such as Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE) are calculated and displayed.

4. **Forecast Display**:
   - The app shows the forecasted prices for the next week, month, and year based on the selected dataset.

5. **Visualization of Forecast Data**:
   - It provides interactive charts displaying the forecasted trends and components (trend, seasonality) using Plotly.

Overall, the app enables users to input a stock ticker, select a dataset, visualize historical data, predict future stock prices, evaluate the model's performance, and view forecasted trends and components.

The dataset is imported from Yahoo finance.
Many modules had been deprecated , so I have made changes.

When using terminal for the code - set the directory using - cd {address of code} - streamlit run main.py
