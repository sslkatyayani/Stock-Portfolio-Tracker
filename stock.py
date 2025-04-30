import yfinance as yf

portfolio = {
    "AAPL": 10,   # 10 shares of Apple
    "MSFT": 5,    # 5 shares of Microsoft
    "GOOGL": 2    # 2 shares of Alphabet
}

total_value = 0
print("Stock Portfolio Tracker\n")

for stock, shares in portfolio.items():
    data = yf.Ticker(stock)
    price = data.history(period="1d")["Close"].iloc[-1]
    value = price * shares
    total_value += value
    print(f"{stock}: {shares} shares x ${price:.2f} = ${value:.2f}")

print(f"\nTotal Portfolio Value: ${total_value:.2f}")