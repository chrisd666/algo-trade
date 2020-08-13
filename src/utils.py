import datetime as dt
from bs4 import BeautifulSoup


def getFinancialYear():
    today = dt.datetime.today()
    current_year = today.year
    date_difference = (dt.date(today.year, 3, 31) -
                       dt.date(today.year, today.month, today.day)).days

    if (date_difference <= 0):
        return current_year + 1
    else:
        return current_year
