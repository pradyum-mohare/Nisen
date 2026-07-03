from src.indicators.engine import IndicatorEngine


class FeatureBuilder:

    @staticmethod
    def build(df):
        """
        Generate all AI features.
        """

        df = IndicatorEngine.calculate_all(df)

        return df