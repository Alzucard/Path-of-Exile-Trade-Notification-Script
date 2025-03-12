\# Introduction

This guide will walk you through setting up a Python script that monitors your client.txt log file in Path of Exile and sends real-time trade messages to your Telegram bot. Never miss a trade request again!

\# Requirements

\* Python 3.x

\* A Telegram bot and chat ID

\* Basic familiarity with running Python scripts

\# Setup Guide

\# Create a Telegram Bot

1. Open Telegram and search for \[u/BotFather\](https://t.me/BotFather).
2. Type /newbot and follow the instructions.
3. Copy the API token given by BotFather.
4. Obtain your chat ID by messaging \[u/userinfobot\](https://t.me/useridinfobot) or using this API request:https://api.telegram.org/botYOUR\\\_BOT\\\_TOKEN/getUpdates

Info: To get the actual chat ID you have to write to the Bot first. There are many tutorials on Stack Overflow on how to get your chat ID.

\# Install Required Libraries

Make sure you have requests and re installed:

pip install requests

pip install re

\# Configure the Script

Update the following values in the script:

API\_TOKEN = 'YOUR\_BOT\_TOKEN'  # Replace with your Bot API token

CHAT\_ID = 'YOUR\_CHAT\_ID'  # Replace with your Telegram chat ID

CLIENT\_LOG\_PATH = '/path/to/client.txt'  # Update with actual path

LOG\_FILE\_PATH = '/path/to/log.txt'  # Update with actual path

\# How It Works

\* The script continuously reads new lines from client.txt.

\* It detects incoming trade requests using a regex pattern.

\* It formats the trade request into a concise message.

\* The message is sent to your Telegram bot.

\* The message is logged into a text file.

\# Run the Script

Save the script as trade\\\_bot.py and run:

python trade\_bot.py

\# Full Script

import requests

import time

import re

from datetime import datetime

\# Telegram Bot Setup

API\_TOKEN = 'YOUR\_BOT\_TOKEN'  # Replace with your Bot API token

CHAT\_ID = 'YOUR\_CHAT\_ID'  # Replace with your Telegram chat ID

TELEGRAM\_URL = f'https://api.telegram.org/bot{API\_TOKEN}/sendMessage'

\# Path to the client.txt file (replace with the correct file path)

CLIENT\_LOG\_PATH = '/path/to/client.txt'

LOG\_FILE\_PATH = '/path/to/log.txt'  # Path to the log file where messages will be saved

\# Function to send messages via Telegram bot

def send\_telegram\_message(message):

payload = {

'chat\_id': CHAT\_ID,

'text': message,

}

response = requests.post(TELEGRAM\_URL, data=payload)

log\_message\_to\_file(message)

return response.json()

\# Function to log messages into a text file

def log\_message\_to\_file(message):

try:

with open(LOG\_FILE\_PATH, 'a') as log\_file:

timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

log\_file.write(f'\[{timestamp}\] {message}\\n')

except Exception as e:

print(f"Error while logging message: {e}")

\# Function to read and monitor the client.txt file

def monitor\_client\_log():

try:

with open(CLIENT\_LOG\_PATH, 'r') as file:

file.seek(0, 2)  # Move to the end of the file (to only read new lines)

while True:

line = file.readline()

if line:

process\_log\_line(line)

else:

time.sleep(5)  # If no new line, wait for 1 second before checking again

except Exception as e:

send\_telegram\_message(f"Error while monitoring client.txt: {str(e)}")

\# Function to process the log lines and clean up the trade message

def process\_log\_line(line):

pattern = r"@From\\s+(\\S+):\\s+Hi, I would like to buy your\\s+(\[\\w\\s%\\-,\]+)\\s+listed for\\s+(\[\\d\\.\]+)\\s+(\[a-zA-Z\\s\]+)\\s+in.\*?(?:stash tab\\s+\\"(\[\^\\"\]+)\\")?"

match = re.search(pattern, line)

if match:

player\_name = match.group(1)

item\_name = match.group(2)

price = match.group(3)

currency\_type = match.group(4).strip()

stash\_tab = match.group(5)

message = f"New trade: {player\_name} is buying {item\_name} for {price} {currency\_type} in stash tab \\"{stash\_tab}\\""

send\_telegram\_message(message)

if \_\_name\_\_ == "\_\_main\_\_":

monitor\_client\_log()

If there are any mistakes please message me.
