# TIME SERIES FORECASTING (ARIMA)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Load dataset
data = pd.read_csv("data.csv")   # replace with your dataset

# Convert date column to datetime (change column name if needed)
data['Date'] = pd.to_datetime(data['Date'])

# Set Date as index
data.set_index('Date', inplace=True)

# Select target column (example: 'Value')
ts = data['Value']

# -------------------------------
# 🔹 VISUALIZE TIME SERIES
# -------------------------------

plt.plot(ts)
plt.title("Time Series Data")
plt.xlabel("Date")
plt.ylabel("Value")
plt.show()

# -------------------------------
# 🔹 BUILD ARIMA MODEL
# -------------------------------

# ARIMA(p,d,q) → example values (1,1,1)
model = ARIMA(ts, order=(1,1,1))
model_fit = model.fit()

print(model_fit.summary())

# -------------------------------
# 🔹 FORECAST FUTURE VALUES
# -------------------------------

forecast = model_fit.forecast(steps=10)

print("\nForecasted Values:\n", forecast)

# -------------------------------
# 🔹 PLOT FORECAST
# -------------------------------

plt.plot(ts, label="Original Data")
plt.plot(forecast, label="Forecast", color='red')
plt.legend()
plt.title("Time Series Forecast")
plt.show()