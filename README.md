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

If there are any mistakes please message me.
