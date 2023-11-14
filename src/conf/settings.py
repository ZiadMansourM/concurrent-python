from typing import Final
from pathlib import Path

BASE_DIR: Final[Path] = Path(__file__).resolve().parent.parent.parent
DATA_DIR: Final[Path] = BASE_DIR.joinpath("data")
LOGS_DIR: Final[Path] = BASE_DIR.joinpath("logs")

__DB_NAME: Final[str] = "tune.db"