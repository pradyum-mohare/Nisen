import pandas as pd

from src.config.settings import (
    MACD_FAST,
    MACD_SLOW,
    MACD_SIGNAL,
)


class MACDIndicator:
    """
    Calculates the Moving Average Convergence Divergence (MACD).

    Outputs:
        - EMA Fast
        - EMA Slow
        - MACD Line
        - Signal Line
        - Histogram
    """

    @staticmethod
    def calculate(
        df: pd.DataFrame,
        fast_period: int = MACD_FAST,
        slow_period: int = MACD_SLOW,
        signal_period: int = MACD_SIGNAL,
    ) -> pd.DataFrame:
        """
        Calculate MACD, Signal Line and Histogram.

        Args:
            df: Market DataFrame containing a 'Close' column.
            fast_period: Fast EMA period.
            slow_period: Slow EMA period.
            signal_period: Signal EMA period.

        Returns:
            DataFrame with MACD-related columns added.
        """

        # Validate MACD settings
        if fast_period >= slow_period:
            raise ValueError(
                "MACD fast period must be smaller than the slow period."
            )

        # Calculate Fast EMA
        fast_ema = (
            df["Close"]
            .ewm(span=fast_period, adjust=False)
            .mean()
        )

        # Calculate Slow EMA
        slow_ema = (
            df["Close"]
            .ewm(span=slow_period, adjust=False)
            .mean()
        )

        # Store EMAs
        df[f"EMA_{fast_period}"] = fast_ema
        df[f"EMA_{slow_period}"] = slow_ema

        # MACD Line
        df["MACD"] = fast_ema - slow_ema

        # Signal Line
        df["Signal"] = (
            df["MACD"]
            .ewm(span=signal_period, adjust=False)
            .mean()
        )

        # Histogram
        df["Histogram"] = (
            df["MACD"] - df["Signal"]
        )

        return df