import streamlit as st
from datetime import date, timedelta
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from chart_studio import plotly
from plotly import graph_objs as go
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title("Stock Prediction App")

user_input = st.text_input("Type the ticker for the stock", "AAPL")
stocks = ["AAPL","GOOG","MSFT","GME"]
stocks.append(user_input)
stocks=tuple(stocks)
selected_stock = st.selectbox("& Select dataset for prediction Or choose from examples", stocks)


n_years = st.slider("Years of prediction", 1 , 4)
period = n_years*365

@st.cache_data
def load_data(ticker):
    data = yf.download(ticker, START,TODAY)
    data.reset_index(inplace=True)
    return data

data_load_state = st.text("Load data....")
data = load_data(selected_stock)
data_load_state.text("Loading data....Done!")

st.subheader('Raw Data')
st.write(data.tail())

def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name='stock_open'))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='stock_close'))
    fig.layout.update(title="Time Series Data" ,xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

plot_raw_data()

# Forecasting 
df_train= data[['Date','Close']]
df_train= df_train.rename(columns={"Date": "ds", "Close":"y"})

m=Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

def evaluate_forecast(true_values, predicted_values):
    mae = mean_absolute_error(true_values, predicted_values)
    rmse = np.sqrt(mean_squared_error(true_values, predicted_values))
    return mae, rmse

# Extract true values and predicted values for the evaluation period
true_values = data['Close'].values[-period:]
predicted_values = forecast['yhat'].values[-period:]

# Calculate evaluation metrics
mae, rmse = evaluate_forecast(true_values, predicted_values)

# Display evaluation metrics
st.subheader('Model Evaluation Metrics')
st.write(f"     Mean Absolute Error (MAE): {mae:.2f}")
st.write(f"     Root Mean Squared Error (RMSE): {rmse:.2f}")

st.subheader('Forecast Data')
st.write(forecast.tail())

current_date = data['Date'].max()
next_week_date = current_date + timedelta(days=7)
next_month_date = current_date + timedelta(days=30)
next_year_date = current_date + timedelta(days=365)

forecast_next_week = forecast[forecast['ds'] == next_week_date]['yhat'].values[0]
forecast_next_month = forecast[forecast['ds'] == next_month_date]['yhat'].values[0]
forecast_next_year = forecast[forecast['ds'] == next_year_date]['yhat'].values[0]

st.subheader('Forecasted Prices')
st.write(f"Next Week: ${forecast_next_week:.2f}")
st.write(f"Next Month: ${forecast_next_month:.2f}")
st.write(f"Next Year: ${forecast_next_year:.2f}")

st.subheader('Forecast data')
fig1=plot_plotly(m, forecast)
st.plotly_chart(fig1)

st.subheader('Forecast components')
fig2= m.plot_components(forecast)
st.write(fig2)