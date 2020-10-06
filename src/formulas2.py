

def MACD(data):
    df = data.copy()

    # FAST MOVING LINE
    df['MA_Fast'] = df['Close'].ewm(span=12, min_periods=12).mean()
    # SLOW MOVING LINE
    df['MA_Slow'] = df['Close'].ewm(span=26, min_periods=26).mean()
    df['MACD'] = df['MA_Fast'] - df['MA_Slow']
    # SIGNAL
    df['Signal'] = df['MACD'].ewm(span=9, min_periods=9).mean()
