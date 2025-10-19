# main.py
import time
import pandas as pd
import alpaca_trade_api as tradeapi
from utils import get_moving_averages, get_last_signal
from config import API_KEY, API_SECRET, BASE_URL

# Initialize Alpaca API
api = tradeapi.REST(API_KEY, API_SECRET, BASE_URL, api_version='v2')

# Choose stock symbol and parameters
SYMBOL = 'AAPL'
SHORT_WINDOW = 50
LONG_WINDOW = 200

def trade_bot():
    print("Starting algorithmic trading bot...\n")

    # Get historical price data
    barset = api.get_bars(
        SYMBOL,
        timeframe="1Week",
        limit=LONG_WINDOW,
        feed="sip"
    ).df

    # ✅ FIXED INDENTATION HERE
    if barset.empty:
        print(f"No data returned for {SYMBOL}. Try a different symbol or timeframe.")
        exit()

    print("Columns returned:", barset.columns)
    print(barset.head())

    # barset = barset[barset['symbol'] == SYMBOL]

    # Compute moving averages
    barset['SMA_SHORT'], barset['SMA_LONG'] = get_moving_averages(barset['Close'], SHORT_WINDOW, LONG_WINDOW)
    signal = get_last_signal(barset)

    print(f"Latest signal: {signal}")

    position = api.list_positions()
    has_position = any(p.symbol == SYMBOL for p in position)

    if signal == "BUY" and not has_position:
        api.submit_order(symbol=SYMBOL, qty=1, side='buy', type='market', time_in_force='gtc')
        print(f"📈 BUY order placed for {SYMBOL}")
    elif signal == "SELL" and has_position:
        api.submit_order(symbol=SYMBOL, qty=1, side='sell', type='market', time_in_force='gtc')
        print(f"📉 SELL order placed for {SYMBOL}")
    else:
        print("No trade action taken.")

# 🟢 This part actually runs the bot
if __name__ == "__main__":
    trade_bot()
