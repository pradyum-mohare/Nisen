import logging
from pathlib import Path
from src.config.settings import LOG_DIR

LOG_DIR.mkdir(exist_ok=True)

log_file = LOG_DIR / "project.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)