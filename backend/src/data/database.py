from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.config.settings import DATABASE_PATH
from src.config.logger import logger


class DatabaseManager:
    """
    Handles all database operations.
    """

    def __init__(self):

        self.engine = create_engine(
            f"sqlite:///{DATABASE_PATH}",
            echo=False
        )

        self.Session = sessionmaker(bind=self.engine)

    def save_market_data(
        self,
        df,
        table_name="nifty_5m"
    ):

        try:

            df.to_sql(
                table_name,
                self.engine,
                if_exists="replace",
                index=True
            )

            logger.info(
                f"Saved {len(df)} rows into '{table_name}'."
            )

        except Exception as e:

            logger.error(f"Database Error: {e}")