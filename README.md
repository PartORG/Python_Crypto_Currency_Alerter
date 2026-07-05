# Crypto Currency Alerter

A simple alert app for changes in cryptocurrencies, built with Python. Stay informed about price fluctuations and get instant notifications when your favorite coins move!

[![Python](https://img.shields.io/badge/python-3.x-blue.svg)] [![License](https://img.shields.io/badge/license-MIT-green.svg)] [![Package Manager](https://img.shields.io/badge/package-manager-pip-orange.svg)]

## Introduction

Crypto Currency Alerter is a lightweight and easy-to-use application designed to monitor cryptocurrency prices in real-time. It alerts you whenever there are significant changes in the price of your favorite coins, helping you stay on top of market trends.

This project is perfect for cryptocurrency enthusiasts who want to be notified about price movements without having to constantly check their portfolios manually.

## Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [Technology Stack](#technology-stack)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [Project Structure](#project-structure)

## Features

### Real-Time Price Monitoring
Crypto Currency Alerter continuously monitors cryptocurrency prices and alerts you when there are significant changes.

### Customizable Alerts
Set up custom alerts for specific coins and price thresholds. You'll receive notifications via the console or any other method you prefer.

### Easy Configuration
Configure the application with a simple configuration file, making it easy to customize without needing to modify the code.

## How It Works

Crypto Currency Alerter uses the CoinGecko API to fetch real-time cryptocurrency prices and compares them against your set thresholds. When a price change exceeds the threshold, an alert is triggered.

Here's a simplified workflow:

1. Fetch current cryptocurrency prices from CoinGecko.
2. Compare prices with user-defined thresholds.
3. Trigger alerts if price changes exceed the thresholds.

## Technology Stack

| Technology | Purpose |
|------------|---------|
| Python     | Main programming language for building the application. |
| CoinGecko API | Used to fetch real-time cryptocurrency prices. |

## Requirements

- Python 3.x
- Internet connection to access the CoinGecko API

## Installation

To install Crypto Currency Alerter, simply run:

```bash
pip install git+https://github.com/PartORG/Python_Crypto_Currency_Alerter.git
```

Alternatively, you can clone the repository and install it manually:

```bash
git clone https://github.com/PartORG/Python_Crypto_Currency_Alerter.git
cd Python_Crypto_Currency_Alerter
pip install -r requirements.txt
```

## Configuration

Crypto Currency Alerter uses a configuration file named `config.yaml`. You can customize the following settings:

- `coins`: List of cryptocurrency symbols to monitor.
- `thresholds`: Price thresholds for triggering alerts.

Example `config.yaml`:

```yaml
coins:
  - BTC
  - ETH
thresholds:
  BTC: 50000
  ETH: 1500
```

## Quick Start

To get started with Crypto Currency Alerter, follow these steps:

1. Clone the repository and install dependencies.
2. Configure your `config.yaml` file with the coins you want to monitor and their price thresholds.
3. Run the application:

```bash
python main.py
```

You should see real-time alerts in the console when there are significant price changes.

## Usage

Crypto Currency Alerter can be used as a standalone application or integrated into other Python scripts for automated monitoring.

Here's an example of how to use it programmatically:

```python
from crypto_data import fetch_prices, check_alerts

# Fetch current prices
prices = fetch_prices()

# Check for alerts based on thresholds
alerts = check_alerts(prices)

if alerts:
    print("Alerts:", alerts)
```

## Project Structure

```
Crypto_Crypto_Currency_Alerter/
├── README.md
├── __pycache__/crypto_data.cpython-312.pyc
├── crypto_data.py
└── main.py
```

- `README.md`: This file.
- `crypto_data.py`: Contains functions for fetching cryptocurrency prices and checking alerts.
- `main.py`: The entry point of the application.

## Development

For development purposes, you can run the application directly from the source code:

```bash
python main.py
```

You can also use a virtual environment to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

## Testing

Crypto Currency Alerter does not currently include automated tests. However, you can manually test the application by running it and checking for alerts.

## Limitations

- The project is a simple example and may not handle all edge cases.
- No external dependencies are used for simplicity.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.