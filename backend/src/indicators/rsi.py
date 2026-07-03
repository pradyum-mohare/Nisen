import pandas as pd

'''The RSI shown on platforms like TradingView often uses Wilder's smoothing, which 
replaces the simple rolling average with an exponential-style smoothing after the initial calculation. 
We'll implement Wilder's RSI later so our values match professional charting platforms more closely.'''
class RSIIndicator:

    @staticmethod
    def calculate(df: pd.DataFrame, period: int = 14):

        df["Change"] = df["Close"].diff()

        df["Gain"] = df["Change"].clip(lower=0)

        df["Loss"] = -df["Change"].clip(upper=0)

        df["Avg_Gain"] = (
            df["Gain"]
            .rolling(window=period)
            .mean()
        )

        df["Avg_Loss"] = (
            df["Loss"]
            .rolling(window=period)
            .mean()
        )

        df["RS"] = df["Avg_Gain"] / df["Avg_Loss"]

        df["RSI"] = 100 - (
            100 / (1 + df["RS"])
        )
        columns_to_drop = ["Change","Gain","Loss","Avg_Gain","Avg_Loss","RS",]

        df.drop(columns=columns_to_drop, inplace=True)


        return df