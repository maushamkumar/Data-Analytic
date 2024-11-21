### Cryptocurrency Analysis Report

**Introduction**
The purpose of this project was to fetch live data for the top 50 cryptocurrencies and analyze it. Key metrics include market capitalization, 24-hour price changes, and trading volumes.

**Insights**
1. Top 5 Cryptocurrencies by Market Cap:
   - Bitcoin: $1.2T
   - Ethereum: $500B
   - Binance Coin: $100B
   - ...

2. Average Price of Top 50 Cryptocurrencies: $X,XXX.XX
3. Highest 24-Hour Price Change: CoinName (+XX%)
4. Lowest 24-Hour Price Change: CoinName (-XX%)

**Challenges Faced**
- Rate limiting from the API.
- Automating updates in Google Sheets.

**Conclusion**
This project successfully demonstrates real-time cryptocurrency data integration and analysis.

# Project Structure
bash '''
project/
│
├── main.py
├── credentials.json      # If required, include the service account credentials
├── analysis_report.pdf
└── README.md
'''

# Cryptocurrency Live Data Analysis

## Description
This project fetches live cryptocurrency data, analyzes it, and displays the results in a live-updating Google Sheet.

## Files
- `main.py`: Python script for fetching and analyzing data.
- `credentials.json`: Service account credentials for Google Sheets (if needed).
- `analysis_report.pdf`: Summary of key findings.

## Google Sheet Link
[Live Google Sheet]([https://docs.google.com/spreadsheets/d/xxxxxxxxxxxx](https://docs.google.com/spreadsheets/d/1yJlKex97GWe7hnmr6HC09MdfmbhqrUh_4TFThOEfHkc/edit?gid=1695350553#gid=1695350553))

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run the script: `python main.py`
