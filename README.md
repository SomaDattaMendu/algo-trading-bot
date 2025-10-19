# Algorithmic Trading Bot using Python and Alpaca API

## Overview

This project implements a simple algorithmic trading bot that utilizes the Alpaca API to automate stock trading based on a moving average crossover strategy. The bot is designed for educational and research purposes and operates in Alpaca’s paper trading environment. It provides a foundation for developing more advanced quantitative trading systems and demonstrates how to integrate financial data, technical indicators, and trade execution through an API.

---

## Objectives

The primary goal of this project is to simulate a rules-based trading strategy using real-time and historical market data. The system:
- Fetches market data through the Alpaca Trading API.
- Calculates short-term and long-term moving averages.
- Generates buy or sell signals based on moving average crossovers.
- Executes trades automatically in a paper trading account.
- Logs outputs for monitoring performance and debugging.

---

## Technical Stack

- **Programming Language:** Python 3  
- **Libraries and Tools:**  
  - `alpaca-trade-api` – for market data and trade execution  
  - `pandas` – for data manipulation and analysis  
  - `time` – for process timing and intervals  

---

# System Workflow

1. **Data Acquisition**  
   Retrieves historical bar data (e.g., 1-day candles) for the selected symbol via the Alpaca Market Data API.

2. **Indicator Calculation**  
   Uses Pandas to compute short- and long-term simple moving averages for the closing price.

3. **Signal Generation**  
   Compares SMAs to determine crossover events that satisfy the entry or exit conditions defined above.

4. **Trade Execution**  
   - Sends a market **BUY** or **SELL** order to the Alpaca Paper Trading API when criteria are met.  
   - Avoids duplicate trades by checking existing positions before executing.

5. **Logging and Validation**  
   Prints system output for every decision step, including market data, SMA values, and actions taken.

