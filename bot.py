
import os
from  dotenv import load_dotenv
from binance import Client
from  binance.exceptions import BinanceAPIException
from binance.enums import *
import logging
import argparse

# logging.basicConfig(level=logging.DEBUG)

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler("bot.log"),
        logging.StreamHandler()
    ]
)

load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')

class BasicBot:
    def __init__(self, api_key, api_secret, args):
        """This the constructor method of this Bot."""
        self.symbol = args.symbol.upper()
        self.side = args.side.upper()
        self.order_type = args.order_type.upper()
        self.quantity = args.quantity
        self.price = args.price
        self.stop_price = args.stop_price

        self.client = Client(api_key, api_secret, testnet=True)
        self.client.FUTURES_URL ='https://testnet.binancefuture.com/fapi'

        exchange_info = self.client.futures_exchange_info()
        self.client._sync_request_time = True

        self.all_symbols = [item['symbol'] for item in exchange_info['symbols']]

        self.app_on = True
        self.start_cli()

    def start_cli(self):
        """Starts the interactive CLI menu for user operations."""
        try:
            while self.app_on:
                option = input('buy/sell(1),options(2) or press ctrl+c for exit: ')
                self.choose_option(option)
                if option.lower() == 'exit':
                    self.app_on = False

        except KeyboardInterrupt:
            logging.info("Exiting. Goodbye!")
            self.app_on = False

    def choose_option(self, options):
        """This method manage the options."""
        if options == '1':
            self.place_order()
        elif options == '2':
            all_options = input('check_connection(1), check_crypto_price(2),'
                                'check_all_available_coins(3): ')
            if all_options == '1':
                self.check_connection()
            elif all_options == '2':
                self.check_crypto_price()
            elif all_options == '3':
                self.get_all_symbols()

        elif options.lower() == 'exit':
            logging.info('Thanks for using our App. See you soon!')

    def check_connection(self):
        """Use this method for check the Connection is good or not."""
        logging.info(self.client.get_server_time())

    def get_all_symbols(self):
        """Get all the Available coins(symbols) in the future test net """
        logging.info("Available Futures Symbols:")
        logging.info(self.all_symbols)

    def check_crypto_price(self):
        """Return current price of the selected coin(symbol)."""
        logging.info(self.client.get_avg_price(symbol=self.symbol))

    def place_order(self):
        """This method is used for placing orders."""

        if self.symbol not in self.all_symbols:
            logging.error(f"Invalid symbol: {self.symbol}")
            exit()

        while True:
            try:
                if self.order_type == 'MARKET':
                    order =self.client.futures_create_order(
                        symbol=self.symbol,
                        side=self.side,
                        type=self.order_type,
                        quantity=self.quantity,
                    )

                if self.order_type == 'LIMIT':
                    if self.price is None:
                        logging.error("Limit order requires --price")
                        return
                    order =self.client.futures_create_order(
                        symbol=self.symbol,
                        side=self.side,
                        type=self.order_type,
                        quantity=self.quantity,
                        timeInForce=TIME_IN_FORCE_GTC,
                        price=self.price,
                    )

                if self.order_type == 'STOP_MARKET':
                    if self.stop_price is None:
                        logging.error("Stop-Market order requires --stop_price")
                        return
                    order =self.client.futures_create_order(
                        symbol=self.symbol,
                        side=self.side,
                        type=self.order_type,
                        quantity=self.quantity,
                        stopPrice=self.stop_price,
                    )

                logging.info(f"Order_id = {order['orderId']}, "
                      f"Coin = {order['symbol']}, "
                      f"Price = {order['price']}, "
                      f"Quantity = {order['origQty']}, "
                      f"Type = {order['type']}, "
                      f"status = {order['status']}, "
                      f"updateTime = {order['updateTime']}, "
                      f"executedQty = {order['executedQty']}, "
                      )

                break
            except BinanceAPIException as e:
                logging.error(e.message)
                if e.code == -1102:
                    logging.error(f'Quantity is very low.Please choose a higher quantity!\nTry again!')
                    exit()


def parse_arguments():
    """This method is used to create the parsers of the bot."""
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

    parser.add_argument('--symbol', type=str, help='Trading pair symbol (e.g., BTCUSDT)', required=True)
    parser.add_argument('--side', type=str, choices=['BUY', 'SELL'], help='Order side', required=True)
    parser.add_argument('--order_type', type=str, choices=['MARKET', 'LIMIT', 'STOP_MARKET'],
                        help='Type of order', required=True)
    parser.add_argument('--quantity', type=float, help='Order quantity', required=True)
    parser.add_argument('--price', type=float, help='Limit price (required if order_type is LIMIT)',
                        default=None)
    parser.add_argument('--stop_price', type=float,
                        help='Stop price (required if order_type is STOP_MARKET)', default=None)

    return parser.parse_args()

if __name__ == '__main__':
    bot = BasicBot(api_key=API_KEY, api_secret=API_SECRET, args=parse_arguments())

