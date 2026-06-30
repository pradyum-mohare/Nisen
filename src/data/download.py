import yfinance as yf
import pandas as pd
from src.data.database import engine
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
    if not validate_dataframe(df):
        return
    if df.empty:
        logger.error("No data downloaded.")
        return

    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

    output_file = RAW_DATA_DIR / "nifty_5m.csv"

    df.to_csv(output_file)


    #to save the data to the database
    df.to_sql("nifty_5m",engine, if_exists="replace",index=True)
    


    logger.info(f"Saved {len(df)} rows.")
    logger.info(f"File saved to {output_file}")

    return df


if __name__ == "__main__":
    download_nifty_data()