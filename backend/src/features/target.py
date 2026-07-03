import pandas as pd


class TargetGenerator:
    """
    Generates target labels for machine learning.
    """

    @staticmethod
    def create(df: pd.DataFrame) -> pd.DataFrame:
        """
        Target:
        1 -> Next candle closes higher.
        0 -> Otherwise.
        """

        df["Target"] = (
            (df["Close"].shift(-1) > df["Close"])
            .astype(int)
        )

        return df