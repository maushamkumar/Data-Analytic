import requests
import pandas as pd
import time
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment
from openpyxl.utils.dataframe import dataframe_to_rows
import threading

class CryptocurrencyTracker:
    def __init__(self, update_interval=300):  # Default update every 5 minutes
        self.update_interval = update_interval
        self.excel_file = 'cryptocurrency_tracker.xlsx'
        self.stop_tracking = False

    def fetch_cryptocurrency_data(self):
        """
        Fetch top 50 cryptocurrencies data from CoinGecko API
        """
        try:
            # Use CoinGecko's API directly
            url = "	CG-RJmRFjREnmXkhWj7RdbXwpiH"
            params = {
                'vs_currency': 'usd',
                'order': 'market_cap_desc',
                'per_page': 50,
                'page': 1,
                'sparkline': 'false',
                'price_change_percentage': '24h'
            }
            
            response = requests.get(url, params=params)
            data = response.json()
            
            # Process and extract required columns
            processed_data = []
            for coin in data:
                processed_data.append({
                    'Cryptocurrency Name': coin['name'],
                    'Symbol': coin['symbol'].upper(),
                    'Current Price (USD)': f"${coin['current_price']:,.2f}",
                    'Market Capitalization': f"${coin['market_cap']:,.0f}",
                    '24-hour Trading Volume': f"${coin['total_volume']:,.0f}",
                    'Price Change (24hr %)': f"{coin['price_change_percentage_24h_in_currency']:.2f}%"
                })
            
            return pd.DataFrame(processed_data)
        
        except Exception as e:
            print(f"Error fetching cryptocurrency data: {e}")
            return pd.DataFrame()

    def create_excel_file(self, df):
        """
        Create or update Excel file with cryptocurrency data
        """
        try:
            # Create a new workbook or load existing
            wb = Workbook()
            ws = wb.active
            ws.title = "Cryptocurrency Data"
            
            # Write DataFrame to worksheet
            for r in dataframe_to_rows(df, index=False, header=True):
                ws.append(r)
            
            # Style the header
            header_font = Font(bold=True)
            for cell in ws[1]:
                cell.font = header_font
                cell.alignment = Alignment(horizontal='center')
            
            # Auto-adjust column widths
            for column in ws.columns:
                max_length = 0
                column_letter = column[0].column_letter
                for cell in column:
                    try:
                        if len(str(cell.value)) > max_length:
                            max_length = len(cell.value)
                    except:
                        pass
                adjusted_width = (max_length + 2)
                ws.column_dimensions[column_letter].width = adjusted_width
            
            # Save the workbook
            wb.save(self.excel_file)
            print(f"Excel file updated at {time.strftime('%Y-%m-%d %H:%M:%S')}")
        
        except Exception as e:
            print(f"Error creating Excel file: {e}")

    def live_update(self):
        """
        Continuously update cryptocurrency data
        """
        while not self.stop_tracking:
            try:
                # Fetch latest data
                df = self.fetch_cryptocurrency_data()
                
                # Update Excel file
                self.create_excel_file(df)
                
                # Wait for next update
                time.sleep(self.update_interval)
            
            except Exception as e:
                print(f"Error in live update: {e}")
                time.sleep(self.update_interval)

    def start_tracking(self):
        """
        Start live tracking in a separate thread
        """
        print("Starting cryptocurrency live tracking...")
        self.tracking_thread = threading.Thread(target=self.live_update)
        self.tracking_thread.start()

    def stop_tracking_thread(self):
        """
        Stop the tracking thread
        """
        self.stop_tracking = True
        if hasattr(self, 'tracking_thread'):
            self.tracking_thread.join()
        print("Tracking stopped.")

def main():
    # Create tracker instance (update every 5 minutes)
    tracker = CryptocurrencyTracker(update_interval=300)
    
    try:
        # Start live tracking
        tracker.start_tracking()
        
        # Keep main thread running
        while True:
            time.sleep(1)
    
    except KeyboardInterrupt:
        # Allow graceful shutdown
        tracker.stop_tracking_thread()

if __name__ == "__main__":
    main()