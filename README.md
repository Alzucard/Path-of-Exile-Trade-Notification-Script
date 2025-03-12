# Trade Notification Bot for Path of Exile

## Introduction

This script monitors your `client.txt` log file in Path of Exile and sends real-time trade messages to your Telegram bot. Never miss a trade request again!

## Requirements

- Python 3.x
- A Telegram bot and chat ID
- Basic familiarity with running Python scripts

## Setup Guide

### Create a Telegram Bot

1. Open Telegram and search for [@BotFather](https://t.me/BotFather).
2. Type `/newbot` and follow the instructions.
3. Copy the API token given by BotFather.
4. Obtain your chat ID by messaging [@userinfobot](https://t.me/useridinfobot) or using this API request:
   ```
   https://api.telegram.org/botYOUR_BOT_TOKEN/getUpdates
   ```
   **Note:** You must send a message to your bot first to retrieve the chat ID. There are many tutorials on Stack Overflow on how to get your chat ID.

### Install Required Libraries

Ensure you have the necessary Python libraries installed:

```sh
pip install requests
```

### Configure the Script

Update the following values in the script before running:

```python
API_TOKEN = 'YOUR_BOT_TOKEN'  # Replace with your Bot API token
CHAT_ID = 'YOUR_CHAT_ID'  # Replace with your Telegram chat ID
CLIENT_LOG_PATH = '/path/to/client.txt'  # Update with actual path
LOG_FILE_PATH = '/path/to/log.txt'  # Update with actual path
```

## How It Works

- The script continuously reads new lines from `client.txt`.
- It detects incoming trade requests using a regex pattern.
- It formats the trade request into a concise message.
- The message is sent to your Telegram bot.
- The message is logged into a text file.

## Run the Script

Save the script as `trade_bot.py` and execute it with:

```sh
python trade_bot.py
```

If you encounter any issues, feel free to open an issue on GitHub or message me.
