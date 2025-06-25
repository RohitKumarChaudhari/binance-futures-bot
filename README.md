# 🐍 Binance Futures Trading Bot (Testnet)

A simplified crypto trading bot built in Python that interacts with the Binance USDT-M Futures Testnet. This project was created as part of a hiring assignment and demonstrates the ability to place market, limit, and stop-market orders using the `python-binance` library.

---

## 🚀 Features

- ✅ Place **Market**, **Limit**, and **Stop-Market** orders
- ✅ Supports **Buy** and **Sell** order sides
- ✅ Fully functional with **Binance Futures Testnet**
- ✅ Command-Line Interface (CLI) for interaction
- ✅ Input validation and error handling
- ✅ Logs all API requests, responses, and errors to `bot.log`
- 🧪 Built with reusability and clarity in mind

---

## 🔧 Requirements

- Python 3.7+
- Binance Futures Testnet Account
- API Key and Secret from [Binance Testnet](https://testnet.binancefuture.com)

Install dependencies:
```bash
pip install -r requirements.txt
```
## 🛠 Setup  
1. Clone the repo:
    ``` bash
    git clone https://github.com/RohitKumarChaudhari/binance-futures-bot.git
    cd binance-futures-bot
    ```
2. Create a .env file:
   ```ini
   API_KEY=your_testnet_api_key
   API_SECRET=your_testnet_api_secret
   ```
3. Run the bot:
    ```bash
    python bot.py --symbol BTCUSDT --side BUY --order_type MARKET --quantity 0.01
    ```
## 💡 CLI Options  
| Argument       | Description                            | Required |
| -------------- | -------------------------------------- | -------- |
| `--symbol`     | Trading pair (e.g., BTCUSDT)           | ✅        |
| `--side`       | BUY or SELL                            | ✅        |
| `--order_type` | MARKET, LIMIT, or STOP\_MARKET         | ✅        |
| `--quantity`   | Order quantity                         | ✅        |
| `--price`      | Price (required for LIMIT orders)      | ❌        |
| `--stop_price` | Stop price (required for STOP\_MARKET) | ❌        |

## 📄 Log File
All actions and errors are logged in bot.log, including:
- Successful API calls
- Order placement results
- Error messages from Binance API

## 📦 File Structure
```
.  
├── bot.py              # Main bot logic  
├── .env                # API credentials  
├── bot.log             # Logging output  
├── README.md           # Documentation  
└── requirements.txt    # Dependencies  
```

## 📌 Notes
- This bot only works with Binance Testnet and should not be used on the mainnet.
- The code is for educational and demonstration purposes.

## 📬 Contact
Rohit Kumar  
Email: rohitkuar13479@gmail.com   
LinkedIn: linkedin.com/in/rohitkumar81  
GitHub: github.com/RohitKumarChaudhari  