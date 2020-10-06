import datetime as dt
from bs4 import BeautifulSoup
import yfinance as yf


def get_financial_year():
    today = dt.datetime.today()
    current_year = today.year
    date_difference = (dt.date(today.year, 3, 31) -
                       dt.date(today.year, today.month, today.day)).days

    if (date_difference <= 0):
        return current_year + 1
    else:
        return current_year


def get_ticker_info(ticker_name, ticker, inr=70):
    yf_ticker_format = ticker_name + ".NS"
    stock = yf.Ticker(yf_ticker_format)
    yf_ticker_info = stock.info

    av_api_key = '2N8UEPVRC2AWTK6B'
    av_base_url = "https://www.alphavantage.co/query?function="
    av_income = av_base_url + "INCOME_STATEMENT&symbol=" + \
        ticker + "&apikey=" + av_api_key
    av_bs = av_base_url + "BALANCE_SHEET&symbol=" + ticker + "&apikey=" + av_api_key

    ticker["beta"] = yf_ticker_info["beta"]
    ticker["close_price"] = yf_ticker_info["regularMarketPreviousClose"]
    ticker["market_cap"] = yf_ticker_info["marketCap"]
    ticker["income"]["interest_expense"] = av_income["annualReports"][0]["interestExpense"] * inr
    ticker["income"]["income_before_tax"] = av_income["annualReports"][0]["incomeBeforeTax"] * inr
    ticker["income"]["income_tax_expense"] = av_income["annualReports"][0]["incomeTaxExpense"] * inr
    ticker["balance_sheet"]["current_liabilities"] = av_bs["annualReports"][0]["totalCurrentLiabilities"] * inr
    ticker["balance_sheet"]["non_current_liabilities"] = av_bs["annualReports"][0]["totalNonCurrentLiabilities"] * inr
    ticker["balance_sheet"]["total_liabilities"] = av_bs["annualReports"][0]["totalLiabilities"] * inr

    return ticker
