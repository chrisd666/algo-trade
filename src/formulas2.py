import pandas as pd
from nsepy import get_history
from datetime import date
import numpy as np


class Ticker:
    def __init__(self, ticker, start_date, end_date):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date

    def get_historical_data(self):
        data = get_history(symbol=self.ticker,
                           start=self.start_date, end=self.end_date)
        data_copy = data.copy()
        filtered_data = data_copy.drop(columns=[
                                       'Series', 'Prev Close', 'Last', 'VWAP', 'Turnover', 'Trades', 'Deliverable Volume', '%Deliverble'])

        return filtered_data


class Indicator:
    def __init__(self, data):
        self.data = data

    def MACD(self, fast=12, slow=26, signal=9):
        df = self.data.copy()

        # FAST MOVING LINE
        df['MA_Fast'] = df['Close'].ewm(span=fast, min_periods=fast).mean()
        # SLOW MOVING LINE
        df['MA_Slow'] = df['Close'].ewm(span=slow, min_periods=slow).mean()
        df['MACD'] = df['MA_Fast'] - df['MA_Slow']
        # SIGNAL
        df['Signal'] = df['MACD'].ewm(span=signal, min_periods=signal).mean()
        df.dropna(inplace=True)

        return df

    def slope(self, ser, n=5):
        import statsmodels.api as sm

        slopes = [i*0 for i in range(n-1)]

        for i in range(n, len(ser)+1):
            y = ser[i-n: i]
            x = np.array(range(n))

            # SCALING
            y_scaled = (y - y.min())/(y.max() - y.min())
            x_scaled = (x - x.min())/(x.max() - x.min())
            x_scaled = sm.add_constant(x_scaled)

            model = sm.OLS(y_scaled, x_scaled)
            results = model.fit()
            slopes.append(results.params[-1])

        slope_angle = np.rad2deg(np.arctan(np.array(slopes)))

        return np.array(slope_angle)
