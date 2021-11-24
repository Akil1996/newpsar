import yfinance as yf
import pandas as pd
import talib
import datetime as dt

def signal_filter(df):
    result_dic = []
    for index, row in df.iterrows():
        if 0 < row.SAR:
            result_dic.append({"dtime": str(index), "open": round(row.open, 2), "high": round(row.high,2), "low": round(row.low, 2), "close": round(row.close,2), "signal": "BUY"})
        if 0 > row.SAR:
            result_dic.append({"dtime": str(index), "open": round(row.open, 2), "high": round(row.high,2), "low": round(row.low, 2), "close": round(row.close,2), "signal": "SELL"})
    return result_dic

def cal_main(symbol, timeFrame, fdate, tdate):
    fromDate = dt.datetime.strptime(fdate, "%Y-%m-%d").date()
    sliceDate = str(fromDate - dt.timedelta(days=100))
    data = yf.download(tickers=symbol, period="ytd", interval="1d", start=sliceDate, end=tdate, group_by='ticker',
                       prepost=True, threads=True, proxy=None)
    data = data.reset_index()
    data.columns = ["dtime", "open", "high", "low", "close", "ac", "volume"]
    df = pd.DataFrame(data)
    df.set_index("dtime", inplace=True)
    df["SAR"] = talib.SAREXT(df.high, df.low, startvalue=0, offsetonreverse=0, accelerationinitlong=0.02, accelerationlong=0.02,
                  accelerationmaxlong=0.20, accelerationinitshort=0.02, accelerationshort=0.02, accelerationmaxshort=0.20)
    df = df.loc[fdate:tdate]
    result_df = signal_filter(df)
    return result_df

def cal_month_main(symbol, timeFrame, fdate, tdate):
    fromDate = dt.datetime.strptime(fdate, "%Y-%m-%d").date()
    sliceDate = str(fromDate - dt.timedelta(days=1000))
    data = yf.download(tickers=symbol, period="ytd", interval="1mo", start=sliceDate, end=tdate, group_by='ticker',
                       prepost=True, threads=True, proxy=None)
    data = data.reset_index()
    data.columns = ["dtime", "open", "high", "low", "close", "ac", "volume"]
    df = pd.DataFrame(data)
    df.set_index("dtime", inplace=True)
    df["SAR"] = talib.SAREXT(df.high, df.low, startvalue=0, offsetonreverse=0, accelerationinitlong=0.02,
                             accelerationlong=0.02,
                             accelerationmaxlong=0.20, accelerationinitshort=0.02, accelerationshort=0.02,
                             accelerationmaxshort=0.20)
    df = df.loc[fdate:tdate]
    result_df = signal_filter(df)
    return result_df

def cal_week_main(symbol, timeFrame, fdate, tdate):
    fromDate = dt.datetime.strptime(fdate, "%Y-%m-%d").date()
    sliceDate = str(fromDate - dt.timedelta(days=1000))
    data = yf.download(tickers=symbol, period="ytd", interval="1wk", start=sliceDate, end=tdate, group_by='ticker',
                       prepost=True, threads=True, proxy=None)
    data = data.reset_index()
    data.columns = ["dtime", "open", "high", "low", "close", "ac", "volume"]
    df = pd.DataFrame(data)
    df.set_index("dtime", inplace=True)
    df["SAR"] = talib.SAREXT(df.high, df.low, startvalue=0, offsetonreverse=0, accelerationinitlong=0.02,
                             accelerationlong=0.02,
                             accelerationmaxlong=0.20, accelerationinitshort=0.02, accelerationshort=0.02,
                             accelerationmaxshort=0.20)
    df = df.loc[fdate:tdate]
    result_df = signal_filter(df)
    return result_df