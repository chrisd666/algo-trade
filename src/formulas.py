import yfinance as yf


def CAPM(beta):
    ten_year_bond_return = 5.91
    ten_year_nifty500_return = 101.35

    capm = (ten_year_bond_return +
            beta * (ten_year_nifty500_return - ten_year_nifty500_return)) * 100

    return capm


def WACC(stock):
    balance_sheet = stock["balance_sheet"]
    income = stock["income"]

    wd = (balance_sheet["total_liabilities"] /
          (balance_sheet["total_liabilities"] + stock["mamrket_cap"])) * 100
    rd = (income["interest_expense"] / (balance_sheet["current_liabilities"] +
                                        balance_sheet["non_current_liabilities"])) * 100
    t = (income["income_tax_expense"] / income["income_before_tax"]) * 100
    we = 100 - wd
    re = stock["capm"]

    wacc = wd * rd * (1 - t) + we * re

    return wacc


dkj = {'zip': '392015', 'sector': 'Basic Materials', 'longBusinessSummary': 'Gujarat Narmada Valley Fertilizers & Chemicals Limited manufactures and markets fertilizers and chemicals in India. It offers fertilizers, such as urea, ammonium nitrophosphate, neem de-oiled cake, and water soluble under the NARMADA brand name. The company also trades in diammonium phosphate, muriate of potash, single super phosphate, ammonium sulphate, and city compost. In addition, it provides industrial chemicals, such as methanol, acetic acid, toluene di Â\x96 isocyanate, aniline, concentrated nitric acid, weak nitric acid, formic acid, ammonium nitrate, ethyl acetate, methyl formate, calcium carbonate, nitrobenzene, and catsol, as well as other products comprising hydrochloric acid, liquid nitrogen, ortho-toluene diamine, meta-toluene diamine, dilute sulphuric acid, dilute nitric acid, and sodium hypochlorite used by a range of manufacturers, processors, and chemical operators. Further, the company offers information technology services consisting of digital signature certificates, eSign, time stamping, e-procurement, e-governance, data center, closed-circuit television surveillance, cloud, software application, authentication, and payment gateway services; and security services, such as managed IT, as well as infrastructure design and building services. The company was formerly known as Gujarat Narmada Valley Fertilizers Co. Ltd. Gujarat Narmada Valley Fertilizers & Chemicals Limited was founded in 1976 and is headquartered in Bharuch, India.', 'city': 'Bharuch', 'phone': '91 26 4224 7001', 'country': 'India', 'companyOfficers': [], 'website': 'http://www.gnfc.in', 'maxAge': 1, 'address1': 'P.O. Narmadanagar', 'fax': '91 26 4224 7084', 'industry': 'Chemicals', 'previousClose': 169.05, 'regularMarketOpen': 170, 'twoHundredDayAverage': 150.24545, 'trailingAnnualDividendYield': 0.029577048, 'payoutRatio': 0.29950002, 'volume24Hr': None, 'regularMarketDayHigh': 173.9, 'navPrice': None, 'averageDailyVolume10Day': 1319137, 'totalAssets': None, 'regularMarketPreviousClose': 169.05, 'fiftyDayAverage': 163.12, 'trailingAnnualDividendRate': 5, 'open': 170, 'toCurrency': None, 'averageVolume10days': 1319137, 'expireDate': None, 'yield': None, 'algorithm': None, 'dividendRate': 5, 'exDividendDate': 1597881600, 'beta': 1.024885,
       'circulatingSupply': None, 'startDate': None, 'regularMarketDayLow': 166.8, 'priceHint': 2, 'currency': 'INR', 'trailingPE': 5.1713066, 'regularMarketVolume': 1172634, 'lastMarket': None, 'maxSupply': None, 'openInterest': None, 'marketCap': 26265804800, 'volumeAllCurrencies': None, 'strikePrice': None, 'averageVolume': 1497923, 'priceToSalesTrailing12Months': 0.50878865, 'dayLow': 166.8, 'ask': 0, 'ytdReturn': None, 'askSize': 0, 'volume': 1172634, 'fiftyTwoWeekHigh': 224.6, 'forwardPE': 2.6966023, 'fromCurrency': None, 'fiveYearAvgDividendYield': None, 'fiftyTwoWeekLow': 95.55, 'bid': 0, 'tradeable': False, 'dividendYield': 0.0296, 'bidSize': 0, 'dayHigh': 173.9, 'exchange': 'NSI', 'shortName': 'GUJARAT NARMADA VA', 'longName': 'Gujarat Narmada Valley Fertilizers & Chemicals Limited', 'exchangeTimezoneName': 'Asia/Kolkata', 'exchangeTimezoneShortName': 'IST', 'isEsgPopulated': False, 'gmtOffSetMilliseconds': '19800000', 'quoteType': 'EQUITY', 'symbol': 'GNFC.NS', 'messageBoardId': 'finmb_878433', 'market': 'in_market', 'annualHoldingsTurnover': None, 'enterpriseToRevenue': 0.487, 'beta3Year': None, 'profitMargins': 0.098409995, 'enterpriseToEbitda': 4.645, '52WeekChange': -0.13683945, 'morningStarRiskRating': None, 'forwardEps': 62.69, 'revenueQuarterlyGrowth': None, 'sharesOutstanding': 155419008, 'fundInceptionDate': None, 'annualReportExpenseRatio': None, 'bookValue': 340.907, 'sharesShort': None, 'sharesPercentSharesOut': None, 'fundFamily': None, 'lastFiscalYearEnd': 1585612800, 'heldPercentInstitutions': 0.19354999, 'netIncomeToCommon': 5080099840, 'trailingEps': 32.69, 'lastDividendValue': None, 'SandP52WeekChange': 0.15364361, 'priceToBook': 0.49588302, 'heldPercentInsiders': 0.42491, 'nextFiscalYearEnd': 1648684800, 'mostRecentQuarter': 1585612800, 'shortRatio': None, 'sharesShortPreviousMonthDate': None, 'floatShares': 88483479, 'enterpriseValue': 25164996608, 'threeYearAverageReturn': None, 'lastSplitDate': None, 'lastSplitFactor': None, 'legalType': None, 'morningStarOverallRating': None, 'earningsQuarterlyGrowth': 1.521, 'dateShortInterest': None, 'pegRatio': None, 'lastCapGain': None, 'shortPercentOfFloat': None, 'sharesShortPriorMonth': None, 'category': None, 'fiveYearAverageReturn': None, 'regularMarketPrice': 170, 'logo_url': 'https://logo.clearbit.com/gnfc.in'}
