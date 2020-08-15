
import requests as req
from bs4 import BeautifulSoup


def scraped_fcf(ticker):
    url_base = "https://www.tickertape.in/stocks"
    url_tail = "financials?period=annual&statement=cashflow"
    url = url_base + "/" + ticker + "/" + url_tail
    response = req.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    column = soup.findAll("div", {"data-row": "cafFcf"})
    free_cash_flows = []

    for i, x in enumerate(column):
        if i == 0:
            continue

        data = BeautifulSoup(str(x), 'html.parser').get_text().replace(',', '')

        if (len(data) > 0):
            free_cash_flows.append(float(data))

    return free_cash_flows


def calculate_growth_rate(free_cash_flows):
    growth_rates = []

    for i in range(len(free_cash_flows)):
        if i < len(free_cash_flows) - 1:
            pct_diff = (free_cash_flows[i+1] -
                        free_cash_flows[i])/abs(free_cash_flows[i])
            growth_rates.append(pct_diff * 100)

    return growth_rates


def generate_forward_fcf(number_of_years, ticker_data, idx, ticker):
    forward_fcf_values = []

    for i in range(number_of_years):
        last_value = ticker_data[idx][ticker]["last_fcf_value"]
        growth_rate = ticker_data[idx][ticker]["avg_growth_rate"]

        if i == 0:
            forward_fcf_values.append(
                last_value + (last_value * growth_rate / 100))
        else:
            last_value = forward_fcf_values[i - 1]

            forward_fcf_values.append(
                last_value + (last_value * growth_rate / 100))

    return forward_fcf_values
