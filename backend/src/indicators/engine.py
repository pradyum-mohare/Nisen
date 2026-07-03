from src.indicators.ema import EMAIndicator
from src.config.settings import EMA_PERIODS
from src.indicators.rsi import RSIIndicator
from src.indicators.macd import MACDIndicator
class IndicatorEngine:

    @staticmethod
    def calculate_all(df):

        df = EMAIndicator.calculate(df, EMA_PERIODS)
        df = RSIIndicator.calculate(df)
        df = MACDIndicator.calculate(df)
        return df