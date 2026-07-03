import pandas as pd
from src.config.logger import logger


def validate_dataframe(df: pd.DataFrame) -> bool:


    if df.empty:
        logger.error("DataFrame is empty.")
        return False

    if df.index.duplicated().sum() > 0:
        logger.warning("Duplicate timestamps found.")

    if df.isnull().sum().sum() > 0:
        logger.warning("Missing values found.")

    if not df.index.is_monotonic_increasing:
        logger.warning("Data is not sorted.")
        df.sort_index(inplace=True)

    logger.info("Data validation completed.")

    return True