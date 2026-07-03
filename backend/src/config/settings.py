from pathlib import Path

# ======================================================
# Project Settings
# ======================================================

# Project Root (backend/)
BASE_DIR = Path(__file__).resolve().parents[2]


# ======================================================
# Directory Settings
# ======================================================

DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
LIVE_DATA_DIR = DATA_DIR / "live"

DATABASE_DIR = BASE_DIR / "database"
DATABASE_PATH = DATABASE_DIR / "market.db"

LOG_DIR = BASE_DIR / "logs"

MODEL_DIR = BASE_DIR / "models"

NOTEBOOK_DIR = BASE_DIR / "notebooks"

TEST_DIR = BASE_DIR / "tests"


# ======================================================
# Market Settings
# ======================================================

NIFTY_SYMBOL = "^NSEI"

DEFAULT_INTERVAL = "5m"

DEFAULT_PERIOD = "60d"


# ======================================================
# Indicator Settings
# ======================================================

EMA_PERIODS = [9, 20, 50, 200]

RSI_PERIOD = 14

MACD_FAST = 12
MACD_SLOW = 26
MACD_SIGNAL = 9


# ======================================================
# Machine Learning Settings
# ======================================================

FEATURE_COLUMNS = [
    "EMA_9",
    "EMA_20",
    "EMA_50",
    "EMA_200",
    "RSI",
    "MACD",
    "Signal",
    "Histogram",
]

TARGET_COLUMN = "Target"

TRAIN_SIZE = 0.8

RANDOM_STATE = 42


# ======================================================
# Debug (Temporary)
# ======================================================

if __name__ == "__main__":
    print(f"BASE_DIR      : {BASE_DIR}")
    print(f"DATA_DIR      : {DATA_DIR}")
    print(f"DATABASE_PATH : {DATABASE_PATH}")
    print(f"MODEL_DIR     : {MODEL_DIR}")