import pandas as pd
import requests
import time
import random
from datetime import datetime

# Sends packets to the server
def send_data(csv_path, server_url, min_delay, max_delay):
    # csv_path - path to csv file
    # server_url - url of the server to which the packets will be sent
    # min_delay and max_delay - in seconds
    try:
        df = pd.read_csv(csv_path)
        print(f"Loaded {len(df)} records from {csv_path}")
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return

    for index, row in df.iterrows():
        # Random delay generation
        delay = random.uniform(min_delay, max_delay)
        time.sleep(delay)

        # Data preparation
        payload = {
            'ip': row['ip address'],
            'latitude': row['Latitude'],
            'longitude': row['Longitude'],
            'timestamp': datetime.now().isoformat(),  # Текущее время
            'suspicious': bool(row['suspicious'])
        }

        # Data sending
        try:
            response = requests.post(
                server_url,
                json=payload,
                timeout=0.1
            )
            print(f"Sent packet {index + 1}/{len(df)}. Status: {response.status_code}. Delay: {delay:.2f}s")
        except Exception as e:
            print(f"Failed to send packet {index + 1}: {str(e)}")


if __name__ == "__main__":
    send_data('./app/ip_addresses.csv', 'http://web:5000/data', 0, 0.01)
    print("Data sending completed!")