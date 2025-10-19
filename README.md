# 🤖 Algorithmic Trading Bot (Python + Alpaca API)

A simple automated trading bot that uses a **Moving Average Crossover Strategy** to generate buy/sell signals and execute trades on **Alpaca's Paper Trading API**.

---

## 🚀 Features
- Fetches live stock data from Alpaca API
- Implements a 50/200-day moving average crossover strategy
- Automatically places paper buy/sell orders
- Logs trade actions and performance

---

## 🧠 Strategy Explanation
- **Buy Signal** → When the 50-day MA crosses above the 200-day MA
- **Sell Signal** → When the 50-day MA crosses below the 200-day MA

---

## ⚙️ Setup Instructions

1. Clone this repo:
   ```bash
   git clone https://github.com/YOUR_USERNAME/algorithmic-trading-bot.git
   cd algorithmic-trading-bot
