import pandas as pd

from src.config.logger import logger
from src.config.settings import RAW_DATA_DIR


class DataLoader:
    """
    Handles loading market data.
    """

    def __init__(self):
        self.file_path = RAW_DATA_DIR / "nifty_5m.csv"

    def load_market_data(self):

        try:

            df = pd.read_csv(
                self.file_path,
                index_col=0,
                parse_dates=True
            )

            logger.info(
                f"Loaded {len(df)} rows."
            )

            return df

        except Exception as e:

            logger.error(e)

            return None