### Cryptocurrency Analysis Report

**Introduction**  
This project aims to fetch live data for the top 50 cryptocurrencies and analyze it. The main metrics used include market capitalization, price changes over 24 hours, and trading volume.

**Insights**
1. **Top 5 Cryptocurrencies by Market Cap**:
   - Bitcoin: $1.2T
   - Ethereum: $500B
   - Binance Coin: $100B
   - ...
   
2. **Average Price of Top 50 Cryptocurrencies**: $X,XXX.XX  
3. **Highest 24-Hour Price Change**: CoinName (+XX%)  
4. **Lowest 24-Hour Price Change**: CoinName (-XX%)

**Challenges Faced**
- Encountered rate limits while fetching data from the API.
- Set up live updates in Google Sheets.

**Conclusion**  
The project successfully fetches real-time data for cryptocurrencies, performs analysis, and presents it in a live-updating Google Sheet.

---

### Project Structure

```bash
project/
│
├── main.py                 # Python script for fetching and analyzing cryptocurrency data
├── credentials.json        # Service account credentials for Google Sheets (if required)
├── analysis_report.pdf     # PDF report summarizing the analysis and insights
└── README.md               # This file, providing instructions and project overview
```

# Cryptocurrency Live Data Analysis

## Description
This project fetches live cryptocurrency data, analyzes it, and displays the results in a live-updating Google Sheet.

## Files
- `main.py`: Python script for fetching and analyzing data.
- `credentials.json`: Service account credentials for Google Sheets (if needed).
- `analysis_report.pdf`: Summary of key findings.

## Google Sheet Link
[Live Google Sheet]([https://docs.google.com/spreadsheets/d/1yJlKex97GWe7hnmr6HC09MdfmbhqrUh_4TFThOEfHkc/edit?gid=1695350553#gid=1695350553])

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run the script: `python main.py`
