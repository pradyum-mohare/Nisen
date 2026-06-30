from pathlib import Path

# Root directory
BASE_DIR = Path(__file__).resolve().parents[2]

# Data folders
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
LIVE_DATA_DIR = DATA_DIR / "live"

# Database
DATABASE_DIR = BASE_DIR / "database"
DATABASE_PATH = DATABASE_DIR / "market.db"

# Logs
LOG_DIR = BASE_DIR / "logs"

# Default symbol
NIFTY_SYMBOL = "^NSEI"

# Default interval
DEFAULT_INTERVAL = "5m"

# Default period
DEFAULT_PERIOD = "60d"