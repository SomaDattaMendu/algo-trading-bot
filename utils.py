# utils.py
import pandas as pd

def get_moving_averages(series, short_window, long_window):
    short_ma = series.rolling(window=short_window).mean()
    long_ma = series.rolling(window=long_window).mean()
    return short_ma, long_ma

def get_last_signal(df):
    if df['SMA_SHORT'].iloc[-1] > df['SMA_LONG'].iloc[-1]:
        return "BUY"
    elif df['SMA_SHORT'].iloc[-1] < df['SMA_LONG'].iloc[-1]:
        return "SELL"
    else:
        return "HOLD"
