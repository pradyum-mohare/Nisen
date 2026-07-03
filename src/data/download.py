import yfinance as yf
import pandas as pd

from src.data.database import DatabaseManager

from src.config.settings import (
    RAW_DATA_DIR,
    NIFTY_SYMBOL,
    DEFAULT_INTERVAL,
    DEFAULT_PERIOD,
)

from src.config.logger import logger
from src.data.validate import validate_dataframe


def download_nifty_data():

    logger.info("Downloading NIFTY data...")

    df = yf.download(
        NIFTY_SYMBOL,
        interval=DEFAULT_INTERVAL,
        period=DEFAULT_PERIOD,
        progress=False
    )

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    if not validate_dataframe(df):
        return

    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

    output_file = RAW_DATA_DIR / "nifty_5m.csv"

    df.to_csv(output_file)

    db = DatabaseManager()
    db.save_market_data(df)

    
    logger.info(f"File saved to {output_file}")

    return df