# filename: stock_plot.py
import sys
import subprocess

# Install required libraries
def install_libraries():
    libraries = ['yfinance', 'matplotlib']
    for library in libraries:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', library])

# Install libraries if not already installed
try:
    import yfinance as yf
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    install_libraries()
    import yfinance as yf
    import matplotlib.pyplot as plt

def plot_stock_price(ticker):
    """
    Plot the stock price of a given ticker symbol.
    
    Parameters:
    ticker (str): The ticker symbol of the stock to plot.
    """
    # Download the stock data
    data = yf.download(ticker, period='1y')

    # Plot the stock price
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data['Close'], label='Close Price')
    plt.title(f'{ticker} Stock Price')
    plt.xlabel('Date')
    plt.ylabel('Price ($)')
    plt.legend()
    plt.show()

# Plot the stock price of NVDA
plot_stock_price('NVDA')