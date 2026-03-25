# Simple Binance Trading Bot

A Python-based CLI tool to place Market and Limit orders on the Binance Futures Testnet.

## Setup
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file in the root directory and add your Binance Testnet API credentials:
   ```text
   BINANCE_API_KEY=your_key
   BINANCE_API_SECRET=your_secret
    ```

4. Get API keys from: https://testnet.binancefuture.com  
   - Register/Login  
   - Go to API Management  
   - Create API Key & Secret  
   - Enable Futures  
   - Add test funds  

---
## Usage
### MARKET Order
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.01
```

## LIMIT ORDER
```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.01 --price 70000
```

## Features
Place MARKET and LIMIT orders
Supports BUY and SELL
CLI-based input
Input validation
Logging of API requests and responses
Error handling

## Logging
Logs are stored in:
bot.log

## Assumptions
Uses Binance Futures Testnet (no real money)
Valid API keys are provided
Sufficient testnet balance is available

## Requirements
Python 3.x
python-binance
python-dotenv