import pandas as pd


class EMAIndicator:

    @staticmethod
    def calculate(df: pd.DataFrame, periods: list[int]):

        for period in periods:

            df[f"EMA_{period}"] = (
                df["Close"]
                .ewm(span=period, adjust=False)
                .mean()
            )

        return df