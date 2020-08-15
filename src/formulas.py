import yfinance as yf


def CAPM(ticker):
    ten_year_bond_return = 5.91
    ten_year_nifty500_return = 101.35
    yf_ticker_format = ticker + ".NS"
    stock = yf.Ticker(yf_ticker_format)
    beta = stock.info["beta"]

    capm = ten_year_bond_return + \
        beta * (ten_year_nifty500_return - ten_year_nifty500_return)

    return capm
