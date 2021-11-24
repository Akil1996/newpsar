import yfinance as yf
import pandas as pd
import talib
import datetime as dt


def psar_profitloss_strategy(stockName, df, fund):
    signal = None
    ePrice = 0
    etime = ""
    result = []
    quantity = 0
    for index, row in df.iterrows():
        if 0 < row.SAR and signal == None:
            quantity = round(fund / row.close)
            ePrice = row.close
            etime = index
            result.append(
                {"entryTime": str(index), "exitTime": "", "entryPrice": row.close, "exitPrice": "", "high": "", "low": "",
                 "indVolatility": "", "volatility": " ", "signal": "BUY", "profit": " ", "profitPercentage": "",
                 "fundSentence": ""})
            signal = "BUY"
        if 0 > row.SAR and signal == "BUY":
            sDf = df.loc[etime: index]
            sDf = sDf[1:]
            dfHigh = sDf["close"].max()
            dfLow = sDf["close"].min()
            exPrice = row.close - ePrice
            purchased = ePrice * quantity
            sold = row.close * quantity
            value1 = ePrice - dfLow
            value2 = value1 / ePrice
            results = value2 * 100
            fundSentence = "Stock" + stockName + str(etime) + " - " + str(index) + " buy for " + str(
                ePrice) + " = " + str(quantity) + "shares. sale on " + str(row.close) + " = " + str(
                quantity) + "shares , purchased " + str(quantity) + "shares at " + str(purchased) + "and sold " + str(
                quantity) + "value of shares = " + str(sold)
            result.append({"entryTime": "", "exitTime": str(index), "entryPrice": "", "exitPrice": row.close, "high": dfHigh,
                           "low": dfLow, "indVolatility": "", "volatility": str(results), "signal": "SELL",
                           "profit": exPrice, "profitPercentage": str(round(((exPrice / row.close) * 100), 2)) + " %",
                           "fundSentence": fundSentence})
            signal = None
    return result


def plreport_main(symbol, fdate, tdate, fund):
    fromDate = dt.datetime.strptime(fdate, "%Y-%m-%d").date()
    sliceDate = str(fromDate - dt.timedelta(days=100))
    data = yf.download(tickers= symbol, period="ytd", interval="1d", start=sliceDate, end=tdate, group_by='ticker',
                       prepost=True, threads=True, proxy=None)
    data = data.reset_index()
    data.columns = ["dtime", "open", "high", "low", "close", "ac", "volume"]
    df = pd.DataFrame(data)
    df.set_index("dtime", inplace=True)
    df['SAR']= talib.SAREXT(df.high, df.low, startvalue=0, offsetonreverse=0, accelerationinitlong=0.02, accelerationlong=0.02,
                      accelerationmaxlong=0.20, accelerationinitshort=0.02, accelerationshort=0.02, accelerationmaxshort=0.20)
    df = df.loc[fdate:tdate]
    df = psar_profitloss_strategy(symbol, df, fund)
    return df

def plreport_month_main(symbol, fdate, tdate, fund):
    fromDate = dt.datetime.strptime(fdate, "%Y-%m-%d").date()
    sliceDate = str(fromDate - dt.timedelta(days=1000))
    data = yf.download(tickers= symbol, period="ytd", interval="1mo", start=sliceDate, end=tdate, group_by='ticker',
                       prepost=True, threads=True, proxy=None)
    data = data.reset_index()
    data.columns = ["dtime", "open", "high", "low", "close", "ac", "volume"]
    df = pd.DataFrame(data)
    df.set_index("dtime", inplace=True)
    df['SAR']= talib.SAREXT(df.high, df.low, startvalue=0, offsetonreverse=0, accelerationinitlong=0.02, accelerationlong=0.02,
                      accelerationmaxlong=0.20, accelerationinitshort=0.02, accelerationshort=0.02, accelerationmaxshort=0.20)
    df = df.loc[fdate:tdate]
    df = psar_profitloss_strategy(symbol, df, fund)
    return df

def plreport_week_main(symbol, fdate, tdate, fund):
    fromDate = dt.datetime.strptime(fdate, "%Y-%m-%d").date()
    sliceDate = str(fromDate - dt.timedelta(days=1000))
    data = yf.download(tickers= symbol, period="ytd", interval="1wk", start=sliceDate, end=tdate, group_by='ticker',
                       prepost=True, threads=True, proxy=None)
    data = data.reset_index()
    data.columns = ["dtime", "open", "high", "low", "close", "ac", "volume"]
    df = pd.DataFrame(data)
    df.set_index("dtime", inplace=True)
    df['SAR']= talib.SAREXT(df.high, df.low, startvalue=0, offsetonreverse=0, accelerationinitlong=0.02, accelerationlong=0.02,
                      accelerationmaxlong=0.20, accelerationinitshort=0.02, accelerationshort=0.02, accelerationmaxshort=0.20)
    df = df.loc[fdate:tdate]
    df = psar_profitloss_strategy(symbol, df, fund)
    return df
