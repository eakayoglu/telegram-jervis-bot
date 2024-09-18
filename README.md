 # telegram-jervis-bot

Jervis is a Telegram bot designed to provide various functionalities such as sending download links, scripts, useful websites, and more. This project is a Python-based Telegram bot that uses `python-telegram-bot`, `requests`, and `lxml` to fetch and provide download links, handle user interaction through inline keyboard buttons, and perform other simple tasks like echoing messages and showing useful websites. The bot's token and other sensitive configurations are managed using the `dotenv` package for security.

This bot returns M-Files VBScript samples (image + txt), M-Files Latest Download Links and M-Files Useful Websites.


## Features

- Send download links in different languages.
- Provide sample scripts.
- Share useful websites.
- Echo messages.
- Retrieve chat IDs.


## Prerequisites

- A Telegram bot token from [BotFather](https://core.telegram.org/bots#botfather)


## Setup

This script automates the setup process for a Python project by performing the following steps:

1. Ensures that the `venv` module is available for creating virtual environments.
2. Creates a virtual environment in the current directory if it does not already exist.
3. Installs the required packages listed in the 'requirements.txt' file.

Usage:
    Run this script directly to automate the setup process:
    ```bash
    python setup.py
    ```

    After running the script, activate the virtual environment:
    ```bash
    source venv/bin/activate
    ```

    To deactivate the virtual environment, run:
    ```bash
    deactivate
    ```


## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/telegram-jervis-bot.git
    cd telegram-jervis-bot
    ```

2. **Create a virtual environment**:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    Create a `.env` file in the root directory and add your Telegram bot token:
    ```env
    BOT_TOKEN_Jervis=your_telegram_bot_token
    ```


## Usage

1. **Run the bot**:
    ```sh
    python jervis.py
    ```

2. **Interact with the bot**:
    - `/start`: Receive a welcome message.
    - `/latest`: Get the latest download links.
    - `/script`: Get a sample script.
    - `/useful_websites`: Receive a list of useful websites.
    - `/get_id`: Retrieve your chat ID.
    - Send any message to get an echo response.


## Environment Variables

- `BOT_TOKEN_Jervis`: Your Telegram bot token.


## Dependencies

- `os`
- `telebot`
- `requests`
- `lxml`
- `dotenv`


## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.


## License

This project is licensed under the MIT License.