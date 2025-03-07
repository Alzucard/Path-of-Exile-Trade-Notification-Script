import requests
import time
import re
from datetime import datetime

# Telegram Bot Setup
API_TOKEN = 'YOUR_BOT_TOKEN'  # Replace with your Bot API token
CHAT_ID = 'YOUR_CHAT_ID'  # Replace with your Telegram chat ID
TELEGRAM_URL = f'https://api.telegram.org/bot{API_TOKEN}/sendMessage'

# Path to the client.txt file (replace with the correct file path)
CLIENT_LOG_PATH = '/path/to/client.txt'
LOG_FILE_PATH = '/path/to/log.txt'  # Path to the log file where messages will be saved

# Function to send messages via Telegram bot
def send_telegram_message(message):
    payload = {
        'chat_id': CHAT_ID,
        'text': message,
    }
    response = requests.post(TELEGRAM_URL, data=payload)
    log_message_to_file(message)
    return response.json()

# Function to log messages into a text file
def log_message_to_file(message):
    try:
        with open(LOG_FILE_PATH, 'a') as log_file:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log_file.write(f'[{timestamp}] {message}\n')
    except Exception as e:
        print(f"Error while logging message: {e}")

# Function to read and monitor the client.txt file
def monitor_client_log():
    try:
        with open(CLIENT_LOG_PATH, 'r') as file:
            file.seek(0, 2)  # Move to the end of the file (to only read new lines)
            while True:
                line = file.readline()
                if line:
                    process_log_line(line)
                else:
                    time.sleep(5)  # If no new line, wait for 1 second before checking again
    except Exception as e:
        send_telegram_message(f"Error while monitoring client.txt: {str(e)}")

# Function to process the log lines and clean up the trade message
def process_log_line(line):
    pattern = r"@From\s+(\S+):\s+Hi, I would like to buy your\s+([\w\s%\-,]+)\s+listed for\s+([\d\.]+)\s+([a-zA-Z\s]+)\s+in.*?(?:stash tab\s+\"([^\"]+)\")?"
    match = re.search(pattern, line)

    if match:
        player_name = match.group(1)
        item_name = match.group(2)
        price = match.group(3)
        currency_type = match.group(4).strip()
        stash_tab = match.group(5)

        message = f"New trade: {player_name} is buying {item_name} for {price} {currency_type} in stash tab \"{stash_tab}\""
        send_telegram_message(message)

if __name__ == "__main__":
    monitor_client_log()
