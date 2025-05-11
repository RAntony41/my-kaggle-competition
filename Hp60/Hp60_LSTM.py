import numpy as np
import pandas as pd
import json
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM

data_file = 'downloaded_data.json'
with open(data_file, 'r') as f:
    raw_data = json.load(f)

df = pd.DataFrame({
    'timestamp': pd.to_datetime(raw_data['datetime'], errors='coerce'),
    'Hp60': raw_data['Hp60']
})
hp60_series = df['Hp60'].dropna()

scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(hp60_series.values.reshape(-1, 1))

def create_sequences(data, time_steps=24):
    X, y = [], []
    for i in range(len(data) - time_steps):
        X.append(data[i:i + time_steps])
        y.append(data[i + time_steps])
    return np.array(X), np.array(y)

time_steps = 24  # Use past 24 hours to predict the next hour
X, y = create_sequences(scaled_data, time_steps)

train_size = int(len(X) * 0.8)
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(time_steps, 1)),
    LSTM(50),
    Dense(1)
])

model.compile(optimizer='adam', loss='mean_squared_error')

history = model.fit(X_train, y_train, epochs=20, batch_size=32, validation_data=(X_test, y_test), verbose=1)

y_pred = model.predict(X_test)
y_pred_inverse = scaler.inverse_transform(y_pred)
y_test_inverse = scaler.inverse_transform(y_test.reshape(-1, 1))

from sklearn.metrics import mean_squared_error
rmse = np.sqrt(mean_squared_error(y_test_inverse, y_pred_inverse))
print(f'RMSE: {rmse:.2f}')

plt.figure(figsize=(10, 6))
plt.plot(hp60_series.index[-len(y_test):], y_test_inverse, label='Actual')
plt.plot(hp60_series.index[-len(y_test):], y_pred_inverse, label='Predicted')
plt.title('LSTM Forecast for Hp60')
plt.xlabel('Datetime')
plt.ylabel('Hp60')
plt.legend()
plt.show()
